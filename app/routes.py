from flask import Blueprint, render_template, request, redirect
from app.models import Post
from .extentions import db



main = Blueprint('main', __name__)



@main.route('/')
def index():
    all_posts = Post.query.order_by(Post.created_at.desc()).all()

    return render_template('index.html', posts=all_posts, select='g')




@main.route('/about/')
def about():
    return render_template('about.html', select='about')


@main.route('/schedule/')
def schedule():
    return render_template('schedule.html', select='schedule')



@main.route('/form/', methods=['GET', "POST"])
def post_form():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        post = Post(
            title=title,
            content=content
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    

    
    else:
        return render_template('post_form.html', select='post_form')
        





# @main.route("/users")
# def users():
#     return render_template("")