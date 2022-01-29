from enum import Enum

from django.db import models
from django.db.models.fields import FloatField


class Nomenclature(models.Model):
    activity = models.IntegerField(default=0)  # kiné:50, ...


class Location(models.Model):
    nomenclature = models.ForeignKey(
        "Nomenclature",
        related_name="locations",
        related_query_name="location",
        on_delete=models.CASCADE,
        null=True,
    )
    raw = models.CharField(max_length=320)  # raw name
    name = models.CharField(max_length=320)  # prettified name

    def __str__(self):
        return self.name


class Patho(models.Model):
    location = models.ForeignKey(
        "Location",
        related_name="pathos",
        related_query_name="patho",
        on_delete=models.CASCADE,
        null=True,
    )
    raw = models.CharField(max_length=320)  # raw name
    name = models.CharField(max_length=320)  # prettified name
    breakpoints_encoded = models.CharField(
        max_length=64, null=True
    )  # encoded breakpoints

    @property
    def durations(self):
        return sorted(
            set([line.duration for line in self.lines.all() if line.duration])
        )

    @property
    def breakpoints(self):
        """Get list of int from encoded to string breakpoints.
        ex: self.breakpoints == '1 10 20'
        """
        if self.breakpoints_encoded:
            return eval(self.breakpoints_encoded)

    @property
    def kinds(self):
        all_kinds = sorted(set([line.kind for line in self.lines.all()]))
        return {
            kind: sorted(
                set(
                    [
                        line.duration
                        for line in [
                            line for line in self.lines.all() if line.kind == kind
                        ]
                    ]
                )
            )
            for kind in all_kinds
        }

    def __str__(self):
        return self.name


class Line(models.Model):

    CODE_KIND_CHOICES = [
        ("INTAKE", "Intake"),
        ("REPORT", "Report"),
        ("CONSULT", "Consultative"),
        ("DOUBLE", "Double"),
        ("SECOND", "Second"),
        ("MLD", "Manual Lymphatic Drainage"),
        ("STANDARD", "Others"),
    ]

    location = models.ForeignKey(
        "timogen.location",
        related_name="lines",
        related_query_name="line",
        on_delete=models.CASCADE,
        null=True,
    )
    patho = models.ForeignKey(
        "timogen.patho",
        related_name="lines",
        related_query_name="line",
        on_delete=models.CASCADE,
        null=True,
    )
    description = models.CharField(max_length=500, null=True)
    kind = models.CharField(max_length=32, choices=CODE_KIND_CHOICES)
    priority = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    code = models.CharField(max_length=10)

    # Fees
    fees = FloatField("Standard Fees")

    # Back Fees - What we should get back
    bfees_c_p = FloatField("Back fees (contracted + privileged)")
    bfees_nc_p = FloatField("Back fees (not contracted + privileged)")
    bfees_c_np = FloatField("Back fees (contracted + not privileged)")
    bfees_nc_np = FloatField("Back fees (not contracted + not privileged)")

    def __str__(self) -> str:
        return f"{self.kind} - {self.duration}min ({self.priority}) [{self.get_all_fees()}]"

    def get_all_fees(self):
        return [
            self.fees,
            self.bfees_c_p,
            self.bfees_nc_p,
            self.bfees_c_np,
            self.bfees_nc_np,
        ]

    def get_bfees(self, contracted, privileged):
        field_name = "bfees_%sc_%sp" % ("n" * (not contracted), "n" * (not privileged))
        return eval("self." + field_name)
