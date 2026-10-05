# Hotel Booking (OOP)

A command-line hotel booking flow that practises object-oriented design:

- `Hotel`: checks availability and books a room (persists to `hotels.csv`)
- `ReservationTicket`: generates the confirmation
- `CreditCard` → `SecureCard`: card validation, extended through inheritance with password authentication

The card files (`cards.csv`, `card_security.csv`) contain **dummy test data only**.

## Run

```bash
pip install -r requirements.txt
python main.py
```
