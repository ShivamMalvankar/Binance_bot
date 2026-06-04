import os
import time
import hmac
import hashlib
import requests

from dotenv import load_dotenv

from bot.logging_config import logger

load_dotenv()


class BinanceClient:

    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self):

        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "API_KEY and API_SECRET must be set"
            )

    def _generate_signature(self, params):

        query_string = "&".join(
            [f"{k}={v}" for k, v in params.items()]
        )

        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, params):

        endpoint = "/fapi/v1/order"

        params["timestamp"] = int(
            time.time() * 1000
        )

        params["signature"] = self._generate_signature(
            params
        )

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        logger.info(
            f"REQUEST -> {params}"
        )

        try:

            response = requests.post(
                self.BASE_URL + endpoint,
                headers=headers,
                params=params,
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            logger.info(
                f"RESPONSE -> {data}"
            )

            return data

        except requests.exceptions.RequestException as e:

            logger.error(
                f"NETWORK/API ERROR -> {str(e)}"
            )

            raise