import pandas as pd
from app import create_app
from app.models import Restaurant, db

app = create_app()

def import_csv():
    with app.app_context():
        # Read CSV (replace 'restaurants.csv' with your file path)
        df = pd.read_csv('restaurants.csv')
        
        # Clear existing data (optional)
        db.session.query(Restaurant).delete()
        
        # Import each row
        for _, row in df.iterrows():
            restaurant = Restaurant(
                name=row['Name'],
                location=row['Location'],
                locality=row['Locality'],
                city=row['City'],
                cuisine=row['Cuisine'],
                rating=float(row['Rating']),
                votes=int(row['Votes']),
                cost=int(row['Cost'])
            )
            db.session.add(restaurant)
        
        db.session.commit()
        print(f"✅ Imported {len(df)} restaurants!")
 

if __name__ == '__main__':
    import_csv()