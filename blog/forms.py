from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from blog.models import Comment


class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      "content",
      Submit('submit', 'Submit')
    )