

from flask import Blueprint , render_template, request
from election.models import Post


main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    # page =request.args.get('page', 1 , type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=6)
    return render_template('home.html')

@main.route("/not_done")
def not_done():
    return render_template('not_done.html')



@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/community")
def community():
    page =request.args.get('page', 1 , type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=6)
    return render_template('community.html', title='Community', posts=posts)
