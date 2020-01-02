from django.db import models
from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitation_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="invitation_received", on_delete=models.CASCADE,
                                verbose_name="User to Invite", help_text="Please select the user you want to play with")
    msg = models.CharField(max_length=300, blank=True, verbose_name="Optional Msg",
                           help_text="Its Good to include a friendly msg")
    timestamp = models.DateTimeField(auto_now_add=True)
