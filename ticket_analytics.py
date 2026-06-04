
"""
Customer Support Ticket Analytics System
"""
import json
import csv
from collections import defaultdict, Counter
from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, customer, priority, category, created_at):
        self.ticket_id = ticket_id
        self.customer = customer
        self.priority = priority
        self.category = category
        self.created_at = created_at
        self.status = "OPEN"

class TicketAnalytics:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def priority_distribution(self):
        return Counter(t.priority for t in self.tickets)

    def category_distribution(self):
        return Counter(t.category for t in self.tickets)

    def export_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ticket_id","customer","priority","category","status"])
            for t in self.tickets:
                writer.writerow([t.ticket_id,t.customer,t.priority,t.category,t.status])

def generate_sample_data():
    analytics = TicketAnalytics()
    for i in range(1, 501):
        analytics.add_ticket(
            Ticket(
                i,
                f"Customer-{i}",
                ["LOW","MEDIUM","HIGH"][i % 3],
                ["Billing","Technical","Account","Sales"][i % 4],
                datetime.now()
            )
        )
    return analytics

if __name__ == "__main__":
    analytics = generate_sample_data()
    print(analytics.priority_distribution())
    print(analytics.category_distribution())
