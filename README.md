# MarketAnalytics
In Progress: Full Discounted Cash Flow &amp; Trading Comparables (Intrinsic vs. Relative) Valuation for US Public companies.


Purpose: I was previously an investment analyst for a ~$6bn AUM fintech / software focused fund. The traditional investment analyst 
and investment banking roles are ripe for analytical support. This project attempts to streamline the discounted cash flow and relative trading comparables build.

I plan to build this project in modules:
- First, establish a consistent historical income statement pull (some specificity of line items will need to be sacrificed for consistency accross statements)
- The same process for the balance sheets and cash flow statements
- Calculate key historical ratios (ROIC, liquidity / solvency, cash yield, etc.)
- Establish an assumptions panel
- Use assumptions to forecast the statements and build a 3-statement operating model
- Construct a DCF exercise on top of the operating model 
- Build comparables sets, and from historicals / forecasts construct a relative trading comparables valuation





The backend server relies on the Alpha Advantage API for reference historical market data, and key dependencies include:
- OpenPyXl

