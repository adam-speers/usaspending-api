from model_mommy import mommy
import pytest


@pytest.fixture
def basic_agencies(db):
    _setup_agency(1, [], "Awarding")

    _setup_agency(4, [], "Funding")


@pytest.fixture
def basic_award(db, basic_agencies):
    mommy.make("awards.Award", id=1, latest_transaction_id=1)
    mommy.make(
        "awards.TransactionNormalized",
        id=1,
        award_id=1,
        awarding_agency_id=1001,
        funding_agency_id=1004,
        federal_action_obligation=5,
        action_date="2020-01-01",
    )


@pytest.fixture
def agencies_with_subagencies(db):
    """Create some agencies with more than one subtier to toptier"""
    _setup_agency(3, [5], "Awarding")

    _setup_agency(2, [6], "Funding")


@pytest.fixture
def subagency_award(db, agencies_with_subagencies):
    mommy.make("awards.Award", id=2, latest_transaction_id=2)

    mommy.make(
        "awards.TransactionNormalized",
        id=2,
        award_id=2,
        awarding_agency_id=1005,
        funding_agency_id=1006,
        federal_action_obligation=10,
        action_date="2020-01-02",
    )


def _setup_agency(id, subtiers, special_name):
    mommy.make(
        "references.ToptierAgency",
        toptier_agency_id=id + 2000,
        name=f"{special_name} Toptier Agency {id}",
        abbreviation=f"TA{id}",
    )
    mommy.make(
        "references.SubtierAgency",
        subtier_agency_id=id + 3000,
        name=f"{special_name} Subtier Agency {id}",
        abbreviation=f"SA{id}",
    )
    mommy.make(
        "references.Agency", id=id + 1000, toptier_agency_id=id + 2000, subtier_agency_id=id + 3000, toptier_flag=True
    )

    for sub_id in subtiers:
        mommy.make(
            "references.SubtierAgency",
            subtier_agency_id=sub_id + 3000,
            name=f"{special_name} Subtier Agency {sub_id}",
            abbreviation=f"SA{sub_id}",
        )
        mommy.make(
            "references.Agency",
            id=sub_id + 1000,
            toptier_agency_id=id + 2000,
            subtier_agency_id=sub_id + 3000,
            toptier_flag=False,
        )


@pytest.fixture
def awards_and_transactions(db):
    # Awards
    mommy.make("awards.Award", id=1, latest_transaction_id=10)
    mommy.make("awards.Award", id=2, latest_transaction_id=20)
    mommy.make("awards.Award", id=3, latest_transaction_id=30)
    mommy.make("awards.Award", id=4, latest_transaction_id=40)
    mommy.make("awards.Award", id=5, latest_transaction_id=50)
    mommy.make("awards.Award", id=6, latest_transaction_id=60)

    # Transaction Normalized
    mommy.make(
        "awards.TransactionNormalized",
        id=10,
        award_id=1,
        federal_action_obligation=5,
        action_date="2020-01-01",
        is_fpds=False,
    )
    mommy.make(
        "awards.TransactionNormalized",
        id=20,
        award_id=2,
        federal_action_obligation=50,
        action_date="2020-01-02",
        is_fpds=False,
    )
    mommy.make(
        "awards.TransactionNormalized",
        id=30,
        award_id=3,
        federal_action_obligation=500,
        action_date="2020-01-03",
        is_fpds=False,
    )
    mommy.make(
        "awards.TransactionNormalized",
        id=40,
        award_id=4,
        federal_action_obligation=5000,
        action_date="2020-01-04",
        is_fpds=True,
    )
    mommy.make(
        "awards.TransactionNormalized",
        id=50,
        award_id=5,
        federal_action_obligation=50000,
        action_date="2020-01-05",
        is_fpds=True,
    )
    mommy.make(
        "awards.TransactionNormalized",
        id=60,
        award_id=6,
        federal_action_obligation=500000,
        action_date="2020-01-06",
        is_fpds=True,
    )

    # Transaction FABS
    mommy.make(
        "awards.TransactionFABS",
        transaction_id=10,
        cfda_number="10.100",
        place_of_perform_country_c="USA",
        place_of_perfor_state_code="SC",
        place_of_perform_county_co="001",
        place_of_perform_county_na="CHARLESTON",
        awardee_or_recipient_legal="RECIPIENT 1",
        awardee_or_recipient_uniqu=None,
    )
    mommy.make(
        "awards.TransactionFABS",
        transaction_id=20,
        cfda_number="20.200",
        place_of_perform_country_c="USA",
        place_of_perfor_state_code="SC",
        place_of_perform_county_co="005",
        place_of_perform_county_na="TEST NAME",
        awardee_or_recipient_legal="RECIPIENT 2",
        awardee_or_recipient_uniqu="456789123",
    )
    mommy.make(
        "awards.TransactionFABS",
        transaction_id=30,
        cfda_number="20.200",
        place_of_perform_country_c="USA",
        place_of_perfor_state_code="WA",
        place_of_perform_county_co="005",
        place_of_perform_county_na="TEST NAME",
        awardee_or_recipient_legal="RECIPIENT 3",
        awardee_or_recipient_uniqu="987654321",
    )

    # Transaction FPDS
    mommy.make(
        "awards.TransactionFPDS",
        transaction_id=40,
        place_of_perform_country_c="USA",
        place_of_performance_state="WA",
        place_of_perform_county_co="005",
        place_of_perform_county_na="TEST NAME",
        awardee_or_recipient_legal="MULTIPLE RECIPIENTS",
        awardee_or_recipient_uniqu="096354360",
    )
    mommy.make(
        "awards.TransactionFPDS",
        transaction_id=50,
        place_of_perform_country_c="USA",
        place_of_performance_state="SC",
        place_of_perform_county_co="001",
        place_of_perform_county_na="CHARLESTON",
        awardee_or_recipient_legal=None,
        awardee_or_recipient_uniqu="123456789",
    )
    mommy.make(
        "awards.TransactionFPDS",
        transaction_id=60,
        place_of_perform_country_c="USA",
        place_of_performance_state="SC",
        place_of_perform_county_co="001",
        place_of_perform_county_na="CHARLESTON",
        awardee_or_recipient_legal=None,
        awardee_or_recipient_uniqu="123456789",
    )

    # References CFDA
    mommy.make("references.Cfda", id=100, program_number="10.100", program_title="CFDA 1")
    mommy.make("references.Cfda", id=200, program_number="20.200", program_title="CFDA 2")

    # Recipient Profile
    mommy.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 1",
        recipient_level="R",
        recipient_hash="2d67171a-1447-ea0a-df99-db8b663f9b07",
    )
    mommy.make(
        "recipient.RecipientProfile", recipient_name="RECIPIENT 2", recipient_level="R", recipient_unique_id="456789123"
    )
    mommy.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 3",
        recipient_level="P",
        recipient_hash="d2894d22-67fc-f9cb-4005-33fa6a29ef86",
        recipient_unique_id="987654321",
    )
    mommy.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 3",
        recipient_level="C",
        recipient_hash="d2894d22-67fc-f9cb-4005-33fa6a29ef86",
        recipient_unique_id="987654321",
    )
    mommy.make(
        "recipient.RecipientProfile",
        recipient_name="MULTIPLE RECIPIENTS",
        recipient_level="R",
        recipient_hash="5bf6217b-4a70-da67-1351-af6ab2e0a4b3",
        recipient_unique_id="096354360",
    )
    mommy.make(
        "recipient.RecipientProfile",
        recipient_name=None,
        recipient_level="R",
        recipient_hash="25f9e794-323b-4538-85f5-181f1b624d0b",
        recipient_unique_id="123456789",
    )

    # Recipient Lookup
    mommy.make(
        "recipient.RecipientLookup",
        legal_business_name="RECIPIENT 3",
        recipient_hash="d2894d22-67fc-f9cb-4005-33fa6a29ef86",
        duns="987654321",
    )
