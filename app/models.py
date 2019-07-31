from app import db
import datetime
from sqlalchemy.orm import validates


def calculate_age(context):
    born = context.get_current_parameters()['dob']
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return "{} years old".format(age)

class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)
    dob = db.Column(db.Date, default=datetime.datetime.utcnow)
    age = db.Column(db.String(20), default=calculate_age)
    rollno = db.Column(db.String(15))

    def __repr__(self):
        return '<Player {}>'.format(self.name)


# player oriented match
class SingleMatch(db.Model):
    __tablename__ = 'singlematch'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index=True, default=datetime.datetime.utcnow)
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    loser_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    # winner_name = db.Column(db.String(30))
    # loser_name = db.Column(db.String(30))

    # @validates('winner_id')
    # def update_winner(self, key, winner_id):
    #     self.winner_name = Player.query.filter_by(id=winner_id).first().name
    #     return winner_id
    #
    # @validates('loser_id')
    # def update_loser(self, key, loser_id):
    #     self.loser_name = Player.query.filter_by(id=loser_id).first().name
    #     return loser_id

    def __repr__(self):
        return '<SingleMatch {}>'.format(self.id)


class DoubleMatch(db.Model):
    __tablename__ = 'doublematch'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index=True, default=datetime.datetime.utcnow)
    winner1_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    winner2_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    loser1_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    loser2_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    # winner1_name = db.Column(db.String(30))
    # winner2_name = db.Column(db.String(30))
    # loser1_name = db.Column(db.String(30))
    # loser2_name = db.Column(db.String(30))

    # @validates('winner1_id')
    # def update_winner1(self, key, winner1_id):
    #     self.winner1_name = Player.query.filter_by(id=winner1_id).first().name
    #     return winner1_id
    #
    # @validates('winner2_id')
    # def update_winner2(self, key, winner2_id):
    #     self.winner2_name = Player.query.filter_by(id=winner2_id).first().name
    #     return winner2_id
    #
    # @validates('loser1_id')
    # def update_loser1(self, key, loser1_id):
    #     self.loser1_name = Player.query.filter_by(id=loser1_id).first().name
    #     return loser1_id
    #
    # @validates('loser2_id')
    # def update_loser2(self, key, loser2_id):
    #     self.loser2_name = Player.query.filter_by(id=loser2_id).first().name
    #     return loser2_id

    def __repr__(self):
        return '<DoubleMatch {}>'.format(self.id)
