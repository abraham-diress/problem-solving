class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        
        for s in emails:
            local, domain = s.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain)) 
        return len(unique)
            
        