from app import app
from models import db, Production

with app.app_context():
    Production.query.delete()

    productions = []

    print("Seeding........")

    p1 = Production(title='P1', genre="Drama", director='John Doe', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor', budget=1000, image="https://www.shutterstock.com/image-photo/mountains-under-mist-morning-amazing-260nw-1725825019.jpg", ongoing=True)

    productions.append(p1)

    p2 = Production(title='P2', genre="Musical", director='John Doe', description='lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor', budget=100000, image="https://www.shutterstock.com/image-photo/mountains-under-mist-morning-amazing-260nw-1725825019.jpg", ongoing=False)

    productions.append(p2)

    p3 = Production(title='P3', genre="Opra", director='John Doe', description='lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor', budget=2000000, image="https://www.shutterstock.com/image-photo/mountains-under-mist-morning-amazing-260nw-1725825019.jpg", ongoing=True) 

    productions.append(p3)

    p4 = Production(title='P4', genre="Action", director='John Doe', description="lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor", budget=200000, image="https://www.shutterstock.com/image-photo/mountains-under-mist-morning-amazing-260nw-1725825019.jpg", ongoing=False)

    productions.append(p4)

    db.session.add_all(productions)
    db.session.commit()

    print("Done seeding.......")