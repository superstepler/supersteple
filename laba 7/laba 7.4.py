class fitness:
    def __init__(self, code_user, year, num_month, duration):
        self.code_user = code_user
        self.year = year
        self.num_month = num_month
        self.duration = duration

    def view_client(self):
        return (f"code_user={self.code_user}, year={self.year}, "
                f"num_month={self.num_month}, duration={self.duration})\n")

fitness_cen = [
    fitness("123", 2024, 6, 12),
    fitness("222", 2025, 4, 24),
    fitness("333", 2023, 8, 8),
    fitness("444", 2024, 2, 12),
    fitness("555", 2025, 5, 32)
]

longest_session = fitness_cen[0]
shortest_session = fitness_cen[0]

for session in fitness_cen:
    if session.duration > longest_session.duration:
        longest_session = session
    if session.duration < shortest_session.duration:
        shortest_session = session

print("Longest session:")
print(longest_session.view_client())

print("Shortest session:")
print(shortest_session.view_client())