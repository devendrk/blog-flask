from flask import Flask, render_template

app = Flask(__name__)
posts = [
  {
    'author':'Don',
    'title': "Test post 1",
    'content': "Test content 1"
  },
  {
    'author':'Don',
    'title': "Test post 2",
    'content': "Test content 2"
  },
  {
    'author':'Don',
    'title': "Test post 3",
    'content': "Test content 3"
  },
]

@app.route('/')
def home():
  return render_template('home.html', posts = posts)

@contact.route('/contact')
def contact():
  return render_template('contact.html')

# should we have a results route?
# @results.route('/results (or search keyword)', methods=['GET', 'POST'])
# def search():
#     form = SearchForm()
#     if form.validate_on_submit():
#         search_term = form.query.data
#         results = Foo.query.all()
#         return render_template('results.html', form=form, results=results)
#     return render_template('results.html', form=form)



if __name__ == "__main__":
  app.run(debug = True)
