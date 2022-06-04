import re


class Security:
    def secure(self, info):
        res = []
        for text in info.split(" "):
            if self.is_social_account_info(text):
                account = text.split("/")[1]
                text = text.replace(account, self.encrypt(account))
            res.append(text)
        return " ".join(res)

    def is_social_account_info(self, param):
        reg = r"[A-Z][a-z]+:www\.[a-z\d.]+\/[a-z\d_]+"
        if re.fullmatch(reg, param):
            return True
        else:
            return False

    def _get_uniform(self, text):
        result = []
        prev = ""
        curr = ""
        for c in text:
            if c == prev:
                curr += c
            else:
                if curr:
                    result.append(curr)
                prev = c
                curr = c
        result.append(curr)
        return result

    def _get_weight(self, text):
        w = ""
        z = 1
        for c in text:
            w += str((ord(c) - 96) * z)
            z += 1
        return w

    def encrypt(self, s):
        uniforms = self._get_uniform(s)
        weights = [self._get_weight(u) for u in uniforms]
        return "".join(weights)
