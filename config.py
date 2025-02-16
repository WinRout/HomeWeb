# Configuration for Spitogatos filters
SPITOGATOS_FILTERS = {
    "listingType": "sale",
    "category": "residential",
    "garage": "true",
    "balcony": "true",
    "elevator": "true",
    "priceHigh": 340000,
    "livingAreaLow": 90,
    "roomsLow": 3,
    "floorNumberLow": 2,
    "constructionYearLow": 1995,
    "areaIDs[]": 2101,
    "sortBy": "datemodified",
    "sortOrder": "desc",
    "offset": 0
}

# Configuration for XE filters
XE_FILTERS = {
    "transaction_name": "buy",
    "item_type": "re_residence",
    "maximum_price": 340000,
    "minimum_size": 90,
    "minimum_bedrooms": 3,
    "minimum_construction_year": 1995,
    "minimum_level": "L2",
    "has_parking": "true",
    "publication_age": 10,
    "sorting": "property_area_in_sq_m_desc",
    "geo_lat_from": 38.02412646276717,
    "geo_lng_from": 23.847762737483777,
    "geo_lat_to": 37.99449479261578,
    "geo_lng_to": 23.805127301826644,
    "maximum_price_per_unit_area": 340000
}

# Base URLs
BASE_URL_SPITOGATOS = 'https://www.spitogatos.gr/aggelia/11{}'
QUERY_URL_SPITOGATOS = "https://www.spitogatos.gr/n_api/v1/properties/search-results"
QUERY_URL_XE = 'https://www.xe.gr/property/results'