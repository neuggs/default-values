# default-values
This project uses a multi-target predictive model to 'guess' at default values for homeowner's insurance quoting.

The data for this project came from Kaggle: https://www.kaggle.com/ycanario/home-insurance

# Data Elements
These elements include all the elements from the Kaggle dataset, some of which are removed because they wouldn't be known at quote or because they had too many missing values.

## Variables Description
* QUOTE_DATE: Day where the quotation was made
* COVER_START: Beginning of the cover payment
* CLAIM3YEARS: 3 last years loss
* P1_EMP_STATUS: Client's professional status
* P1_PT_EMP_STATUS: Client's part-time professional status
* BUS_USE: Commercial use indicator
* CLERICAL: Administration office usage indicator
* AD_BUILDINGS: Building coverage - Self damage
* RISK_RATED_AREA_B: Geographical Classification of Risk - Building
* SUM_INSURED_BUILDINGS: Assured Sum - Building
* NCD_GRANTED_YEARS_B: Bonus Malus - Building
* AD_CONTENTS: Coverage of personal items - Self Damage
* RISK_RATED_AREA_C: Geographical Classification of Risk - Personal Objects
* SUM_INSURED_CONTENTS: Assured Sum - Personal Items
* NCD_GRANTED_YEARS_C: Malus Bonus - Personal Items
* CONTENTS_COVER: Coverage - Personal Objects indicator
* BUILDINGS_COVER: Cover - Building indicator
* SPEC_SUM_INSURED: Assured Sum - Valuable Personal Property
* SPEC_ITEM_PREM: Premium - Personal valuable items
* UNSPEC_HRP_PREM: Unknown
* P1_DOB: Date of birth of the client
* P1_MAR_STATUS: Marital status of the client
* P1_POLICY_REFUSED: Police Emission Denial Indicator
* P1_SEX: customer sex
* APPR_ALARM: Appropriate alarm
* APPR_LOCKS: Appropriate lock
* BEDROOMS: Number of bedrooms
* ROOF_CONSTRUCTION: Code of the type of construction of the roof
* WALL_CONSTRUCTION: Code of the type of wall construction
* FLOODING: House susceptible to floods
* LISTED: National Heritage Building
* MAX_DAYS_UNOCC: Number of days unoccupied
* NEIGH_WATCH: Vigils of proximity present
* OCC_STATUS: Occupancy status
* OWNERSHIP_TYPE: Type of membership
* PAYING_GUESTS: Presence of paying guests
* PROP_TYPE: Type of property
* SAFE_INSTALLED: Safe installs
* SEC_DISC_REQ: Reduction of premium for security
* SUBSIDENCE: Subsidence indicator (relative downwards motion of the surface )
* YEARBUILT: Year of construction
* CAMPAIGN_DESC: Description of the marketing campaign
* PAYMENT_METHOD: Method of payment
* PAYMENT_FREQUENCY: Frequency of payment
* LEGAL_ADDON_PRE_REN: Option "Legal Fees" included before 1st renewal
* LEGAL_ADDON_POST_REN: Option "Legal Fees" included after 1st renewal
* HOME_EM_ADDON_PRE_REN: "Emergencies" option included before 1st renewal
* HOME_EM_ADDON_POST_REN: Option "Emergencies" included after 1st renewal
* GARDEN_ADDON_PRE_REN: Option "Gardens" included before 1st renewal
* GARDEN_ADDON_POST_REN: Option "Gardens" included after 1st renewal
* KEYCARE_ADDON_PRE_REN: Option "Replacement of keys" included before 1st renewal
* KEYCARE_ADDON_POST_REN: Option "Replacement of keys" included after 1st renewal
* HP1_ADDON_PRE_REN: Option "HP1" included before 1st renewal
* HP1_ADDON_POST_REN: Option "HP1" included after 1st renewal
* HP2_ADDON_PRE_REN: Option "HP2" included before 1st renewal
* HP2_ADDON_POST_REN: Option "HP2" included afterrenewal
* HP3_ADDON_PRE_REN: Option "HP3" included before 1st renewal
* HP3_ADDON_POST_REN: Option "HP3" included after renewal
* MTA_FLAG: Mid-Term Adjustment indicator
* MTA_FAP: Bonus up to date of Adjustment
* MTA_APRP: Adjustment of the premium for Mid-Term Adjustmen
* MTA_DATE: Date of Mid-Term Adjustment
* LAST_ANN_PREM_GROSS: Premium - Total for the previous year
* POL_STATUS: Police status
* Police: Police number
 
