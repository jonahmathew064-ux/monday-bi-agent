import requests
import pandas as pd
import os
API_KEY = os.getenv("MONDAY_API_KEY")
# Board IDs from your Monday workspace
DEALS_BOARD_ID = 5027108732
WORK_ORDERS_BOARD_ID = 5027108789

# Monday API endpoint
url = "https://api.monday.com/v2"

# Request headers
headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}


def fetch_board(board_id):

    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page(limit: 100) {{
          items {{
            name
            column_values {{
              text
              column {{
                title
              }}
            }}
          }}
        }}
      }}
    }}
    """

    try:
        response = requests.post(url, json={"query": query}, headers=headers)
        data = response.json()

        # Handle API authentication errors
        if "data" not in data:
            raise Exception(f"Monday API Error: {data}")

        boards = data["data"]["boards"]

        if not boards:
            raise Exception("No board found. Check BOARD_ID or permissions.")

        items = boards[0]["items_page"]["items"]

        rows = []

        for item in items:

            row = {"Name": item["name"]}

            for col in item["column_values"]:
                row[col["column"]["title"]] = col["text"]

            rows.append(row)

        df = pd.DataFrame(rows)

        return df

    except Exception as e:
        raise Exception(f"Error fetching board data: {e}")


def fetch_deals():
    return fetch_board(DEALS_BOARD_ID)


def fetch_work_orders():

    return fetch_board(WORK_ORDERS_BOARD_ID)

