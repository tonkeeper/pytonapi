from typing import Dict, Any

from pytonapi.schema.gasless import GaslessConfig, SignRawParams
from pytonapi.tonapi.client import TonapiClient


class GaslessMethod(TonapiClient):

    def get_config(self) -> GaslessConfig:
        """
        Returns configuration of gasless transfers.

        :return: :class:`GaslessConfig`
        """
        method = "v2/gasless/config"
        response = self._get(method=method)

        return GaslessConfig(**response)

    def estimate_gas_price(self, master_id: str, body: Dict[str, Any]) -> SignRawParams:
        """
        Returns estimated gas price.

        :param master_id: Jetton Master ID.
        :param body: The body should contain a JSON object with the following structure:
                    {
                      "wallet_address": "string",
                      "wallet_public_key": "string",
                      "messages": [
                        {
                          "boc": "string"
                        }
                      ]
                    }
        :return: :class:`int`
        """
        method = f"v2/gasless/estimate/{master_id}"
        response = self._post(method=method, body=body)

        return SignRawParams(**response)

    def send(self, body: Dict[str, Any]) -> bool:
        """
        Send message to blockchain.

        :param body: The body should contain a JSON object with the following structure:
                     {
                       "wallet_public_key": "string",  # The public key of the wallet.
                       "boc": "string"  # A single BOC or a batch of BOCs serialized in base64.
                     }
        :return: bool
        """
        method = "v2/gasless/send"
        response = self._post(method=method, body=body)

        return bool(response)
