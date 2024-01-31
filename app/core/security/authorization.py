from fastapi import Request


from .tokens import get_access_token_from_cookie


async def authorization_optional(request: Request):
    data = get_access_token_from_cookie(request)
    return data.get("user_id")
