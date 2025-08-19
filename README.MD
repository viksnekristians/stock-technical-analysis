# Stock Technical Analysis

## Quick Start

1. **Make wait-for-it.sh executable:**
   ```sh
   chmod +x wait-for-it.sh
   ```

2. **Build and start all services:**
   ```sh
   docker compose up --build
   ```

3. **Run Django migrations inside the app container:**
   ```sh
   docker exec -it stock-technical-analysis bash
   python manage.py migrate
   ```

## Data Management

- **Manual Asset Entry:**  
  Add assets directly in the `a_assets` table using phpMyAdmin:  
  [http://localhost:8080/](http://localhost:8080/)

  Example asset with data available at Alphavantage:  
  - Symbol: `IBM`  
  - Name: `International Business Machines Corporation`

- **Daily Data Import:**  
  Use the management command to import daily data for existing assets:
  ```sh
  python manage.py daily_data_import
  ```
  (Run this inside the app container.)  
  _It is also scheduled as a cronjob at 8am and 8pm server time.

- **Alphavantage API** is used for asset data fetching.

## AI Summary (Optional)

- **Pull the Llama3 model inside the Ollama container:**
  ```sh
  docker exec -it ollama ollama pull llama3
  ```

## Usage

- Visit:  
  [http://localhost:8000/assets/asset_info/<asset id>](http://localhost:8000/assets/asset_info/<asset id>)  
  to view the asset price graph and optionally generate an AI summary.

---