# Copilot Instructions for `ba_course`

## Project Overview
This project contains SQL scripts for querying and managing data related to airports, hotels, and restaurants. The codebase is organized by domain, with each subdirectory containing SQL files for a specific area:
- `Airport/airportquery.sql`: Queries for airplane, flight, airline, and airport data.
- `hotels_restaurants/query.sql`: Queries and DDL for restaurants, users, reviews, and hotels.

## Key Patterns & Conventions
- **Directory Structure**: Each domain (e.g., Airport, hotels_restaurants) has its own folder. Place new SQL scripts in the relevant domain folder.
- **SQL Style**: Queries use explicit JOINs and often reference multiple tables. Use clear table aliases and prefer explicit JOIN syntax over implicit joins.
- **Data Manipulation**: Both SELECT and DML (UPDATE, DELETE) statements are present. DDL (CREATE TABLE) is included for hotels.
- **Schema References**: Some queries reference a schema prefix (e.g., `exploreplaces.restaurants`). Maintain this convention for cross-schema queries.
- **Date Filtering**: Use SQL date functions (e.g., `YEAR()`, `MONTH()`) for filtering by year/month.
- **Sample Data Patterns**: Example queries filter by city, age, or review content. Follow these patterns for new queries.

## Developer Workflows
- **No build/test automation**: This repo is a collection of SQL scripts. There are no build, test, or CI/CD workflows defined.
- **Manual Execution**: Run SQL scripts manually in your preferred SQL client against the appropriate database.
- **No external dependencies**: The project does not use external libraries or frameworks.

## Examples
- To add a new query for hotels, create a new `.sql` file in `hotels_restaurants/` or append to `query.sql`.
- To extend airport data queries, update `Airport/airportquery.sql` using explicit JOINs as shown.

## Additional Notes
- There is no `.github/copilot-instructions.md` prior to this version.
- The `README.md` is minimal; this file is the primary source for project-specific AI guidance.

---
For questions or to clarify conventions, review the existing SQL files for examples of preferred patterns.
