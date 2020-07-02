from django.db.models import Q, Sum, Count, F, Value, Case, When
from django.db.models.functions import Coalesce, Concat
from rest_framework.response import Response

from usaspending_api.awards.models import FinancialAccountsByAwards
from usaspending_api.common.cache_decorator import cache_response
from usaspending_api.disaster.v2.views.disaster_base import DisasterBase, AwardTypeMixin


class AmountViewSet(AwardTypeMixin, DisasterBase):
    """View to implement the API"""

    endpoint_doc = "usaspending_api/api_contracts/contracts/v2/disaster/award/amount.md"

    @cache_response()
    def post(self, request):
        return Response(self.queryset)

    @property
    def queryset(self):
        filters = [
            Q(disaster_emergency_fund__in=self.def_codes),
            Q(treasury_account__federal_account__isnull=False),
            Q(treasury_account__isnull=False),
            self.all_closed_defc_submissions,
        ]

        count_field = Concat("piid", "fain", "uri")
        if self.award_type_codes:
            filters.extend([Q(award__type__in=self.award_type_codes), Q(award__isnull=False)])
            count_field = "award_id"

        fields = {
            "count": Count(count_field, distinct=True),
            "obligation": Coalesce(Sum("transaction_obligated_amount"), 0),
            "outlay": Coalesce(
                Sum(
                    Case(
                        When(self.final_submissions_query_filters, then=F("gross_outlay_amount_by_award_cpe")),
                        default=Value(0),
                    )
                ),
                0,
            ),
        }

        return FinancialAccountsByAwards.objects.filter(*filters).aggregate(**fields)
