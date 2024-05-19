from py_near.account import Account
import asyncio
from py_near.dapps.core import NEAR

ACCOUNT_ID = "stalat.testnet"
PRIVATE_KEY = "ed25519:t72B9cNxmk2SkRbqvUKewLqwKDzrgyiLYbbJYnb37cFNuxcm81UJYz99UUxkSw5opwCSfPXXw1u8CQ3Lz8eC38i"


async def main():
   acc = Account(ACCOUNT_ID, PRIVATE_KEY)

   await acc.startup()
   print(await acc.get_balance() / NEAR)
   print(await acc.get_balance("stalat.testnet") / NEAR)

   tr = await acc.send_money("stalat.testnet", NEAR * 2)
   print(tr.transaction.hash)
   print(tr.logs)


asyncio.run(main())