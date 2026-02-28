from fastapi import Request, HTTPException, status
import re

class SecurityGuard:
    def __init__(self, check_sql=True, check_xss=True):
        self.check_sql = check_sql
        self.check_xss = check_xss

    async def __call__(self, request: Request, call_next):
        # রিকোয়েস্টের বডি এবং ইউআরএল চেক করা
        body = await request.body()
        body_str = body.decode("utf-8")
        url = str(request.url)
        
        combined_data = body_str + url

        if self.check_sql:
            if self._is_sql_injection(combined_data):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Potential SQL Injection detected!"
                )

        if self.check_xss:
            if self._is_xss(combined_data):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Potential XSS attack detected!"
                )

        response = await call_next(request)
        return response

    def _is_sql_injection(self, data):
        # বেসিক SQL ইনজেকশন প্যাটার্ন
        patterns = [
            r"SELECT .* FROM",
            r"DROP TABLE",
            r"UNION SELECT",
            r"INSERT INTO",
            r"OR '1'='1'"
        ]
        for pattern in patterns:
            if re.search(pattern, data, re.IGNORECASE):
                return True
        return False

    def _is_xss(self, data):
        # বেসিক XSS প্যাটার্ন
        patterns = [
            r"<script.*?>",
            r"javascript:",
            r"onerror="
        ]
        for pattern in patterns:
            if re.search(pattern, data, re.IGNORECASE):
                return True
        return False
      
