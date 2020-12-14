DROP VIEW IF EXISTS award_delta_view;

CREATE VIEW award_delta_view AS
SELECT
  "award_id",
  "generated_unique_award_id",
  "display_award_id",

  "category",
  "type",
  "type_description",
  "piid",
  "fain",
  "uri",
  "total_obligation",
  "description",
  "award_amount",
  "total_subsidy_cost",
  "total_loan_value",
  "update_date",

  "recipient_name",
  "recipient_unique_id",
  "recipient_hash",
  "recipient_levels",

  "parent_recipient_unique_id",
  "business_categories",

  "action_date",
  "fiscal_year",
  "last_modified_date",
  "period_of_performance_start_date",
  "period_of_performance_current_end_date",
  "date_signed",
  "ordering_period_end_date",

  "original_loan_subsidy_cost",
  "face_value_loan_guarantee",

  "awarding_agency_id",
  "funding_agency_id",
  "funding_toptier_agency_id",
  "funding_subtier_agency_id",
  "awarding_toptier_agency_name",
  "funding_toptier_agency_name",
  "awarding_subtier_agency_name",
  "funding_subtier_agency_name",
  "awarding_toptier_agency_code",
  "funding_toptier_agency_code",
  "awarding_subtier_agency_code",
  "funding_subtier_agency_code",

  "recipient_location_country_code",
  "recipient_location_country_name",
  "recipient_location_state_code",
  "recipient_location_state_name",
  "recipient_location_state_fips",
  "recipient_location_state_population",
  "recipient_location_county_code",
  "recipient_location_county_name",
  "recipient_location_county_population",
  "recipient_location_congressional_code",
  "recipient_location_congressional_population",
  "recipient_location_zip5",
  "recipient_location_city_name",

  "pop_country_code",
  "pop_country_name",
  "pop_state_code",
  "pop_state_name",
  "pop_state_fips",
  "pop_state_population",
  "pop_county_code",
  "pop_county_name",
  "pop_county_population",
  "pop_zip5",
  "pop_congressional_code",
  "pop_congressional_population",
  "pop_city_name",
  "pop_city_code",

  "cfda_number",
  "cfda_program_title" as cfda_title,

  "sai_number",
  "type_of_contract_pricing",
  "extent_competed",
  "type_set_aside",

  "product_or_service_code",
  "product_or_service_description",
  "naics_code",
  "naics_description",

  "tas_paths",
  "tas_components",
  "disaster_emergency_fund_codes",
  "total_covid_outlay",
  "total_covid_obligation"

FROM "vw_es_award_search";
