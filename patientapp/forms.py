from .models import *
from django.forms import DateInput
from django.forms.fields import DateField
from django.forms.widgets import PasswordInput
from django import forms
from django.forms import DateInput, DateField, PasswordInput

      
            
class MedicalTreatmentForm(forms.ModelForm):
    treatment = forms.ModelMultipleChoiceField(queryset=Treatment.objects.all(), widget=forms.CheckboxSelectMultiple)
    review_of_systems = forms.ModelMultipleChoiceField(queryset=ReviewofSystem.objects.all(), widget=forms.CheckboxSelectMultiple)
    examination = forms.ModelMultipleChoiceField(queryset=Examination.objects.all(), widget=forms.CheckboxSelectMultiple)
    diagnosis = forms.ModelMultipleChoiceField(queryset=Diagnosis.objects.all(), widget=forms.CheckboxSelectMultiple)
    investigation = forms.ModelMultipleChoiceField(queryset=Investigation.objects.all(), widget=forms.CheckboxSelectMultiple)
    medication = forms.ModelMultipleChoiceField(queryset=Medication.objects.all(), widget=forms.CheckboxSelectMultiple)
    consultation = forms.ModelMultipleChoiceField(queryset=Consultation.objects.all(), widget=forms.CheckboxSelectMultiple)
    follow_up_date = DateField(widget=DateInput)
    class Meta:
        model = Medical_History
        fields = ('__all__')

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={
        
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'user_type']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
    



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['profile_image', 'city', 'address', 'country', 'date_of_birth', 'blood_group', 'gender']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['address', 'profile_image', 'gender', 'description']

class DoctorSpecilizationForm(forms.ModelForm):
    class Meta:
        model = DoctorSpecialization
        fields = ['doctor_category',]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'upload'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control select'
        self.fields['description'].widget.attrs['class'] = 'form-control'



class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistoryy
        fields = [
            'reason',
            'weight',
            'other_illness',
            'other_information',
        ]

    def __init__(self, *args, **kwargs):
        super(MedicalHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


from django import forms

class FamilyMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = FamilyMedicalHistory
        fields = [
            'medical_condition',
            'affected_member_name',
            'relationship',
        ]

    def __init__(self, *args, **kwargs):
        super(FamilyMedicalHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import CurrentMedication

class CurrentMedicationForm(forms.ModelForm):
    class Meta:
        model = CurrentMedication
        fields = [
            'medicine_name',
            'reason',
            'date',
        ]

    def __init__(self, *args, **kwargs):
        super(CurrentMedicationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import Allergy

class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = [
            'allergy_name',
            'severity',
            'diagnosis_date',
        ]

    def __init__(self, *args, **kwargs):
        super(AllergyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import Surgery

class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = [
            'surgery_type',
            'surgery_date',
            'reason',
        ]

    def __init__(self, *args, **kwargs):
        super(SurgeryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import ImmunizationHistory

class ImmunizationHistoryForm(forms.ModelForm):
    class Meta:
        model = ImmunizationHistory
        fields = [
            'vaccine_name',
            'date',
        ]

    def __init__(self, *args, **kwargs):
        super(ImmunizationHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class FamilyMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = FamilyMedicalHistory
        fields = [
            'medical_condition',
            'affected_member_name',
            'relationship',
        ]

    def __init__(self, *args, **kwargs):
        super(FamilyMedicalHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms
from .models import LabReport

class LabReportForm(forms.ModelForm):
    class Meta:
        model = LabReport
        exclude = ['patient', 'doctor']  # Exclude patient and doctor fields from the form

from django import forms
from .models import ChiefComplaint

class ChiefComplaintForm(forms.ModelForm):
    class Meta:
        model = ChiefComplaint
        fields = ['chief_complaint_text', 'history_presenting_complaint_text']
        # Add any additional fields or customize fields as needed

# In forms.py
class HospitalHistoryForm(forms.ModelForm):
    class Meta:
        model = HospitalHistory
        fields = ['surgical_history', 'family_history', 'social_history', 'pediatric_history', 'obstetric_history']
        # Add any additional fields or customize fields as needed

from django import forms
from .models import Examination, Investigations, Vitals, LabTest

class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['examination_name', 'description', 'date']

class InvestigationsForm(forms.ModelForm):
    class Meta:
        model = Investigations
        fields = ['investigation_name', 'description', 'date']

class VitalsForm(forms.ModelForm):
    class Meta:
        model = Vitals
        fields = ['vital_name', 'value', 'unit']

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['test_name', 'result', 'date', 'file_upload']



from django.shortcuts import render, get_object_or_404, redirect
from .models import Examination, Investigations, Vitals, LabTest
from .forms import ExaminationForm, InvestigationsForm, VitalsForm, LabTestForm

def enter_examination(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = ExaminationForm(request.POST)
        if form.is_valid():
            examination = form.save(commit=False)
            examination.patient = patient
            examination.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = ExaminationForm()

    saved_examinations = Examination.objects.filter(patient=patient)

    context = {
        'form': form,
        'patient': patient,
        'saved_examinations': saved_examinations,
    }

    return render(request, 'today/enter_examination.html', context)

def enter_investigations(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = InvestigationsForm(request.POST)
        if form.is_valid():
            investigation = form.save(commit=False)
            investigation.patient = patient
            investigation.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = InvestigationsForm()

    saved_investigations = Investigations.objects.filter(patient=patient)

    context = {
        'form': form,
        'patient': patient,
        'saved_investigations': saved_investigations,
    }

    return render(request, 'today/enter_investigations.html', context)

def enter_vitals(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = VitalsForm(request.POST)
        if form.is_valid():
            vital = form.save(commit=False)
            vital.patient = patient
            vital.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = VitalsForm()

    saved_vitals = Vitals.objects.filter(patient=patient)

    context = {
        'form': form,
        'patient': patient,
        'saved_vitals': saved_vitals,
    }

    return render(request, 'today/enter_vitals.html', context)

def enter_labtest(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = LabTestForm(request.POST, request.FILES)
        if form.is_valid():
            lab_test = form.save(commit=False)
            lab_test.patient = patient
            lab_test.save()
            return redirect('patient_details', patient_id=patient_id)
    else:
        form = LabTestForm()

    saved_lab_tests = LabTest.objects.filter(patient=patient)

    context = {
        'form': form,
        'patient': patient,
        'saved_lab_tests': saved_lab_tests,
    }

    return render(request, 'today/enter_labtest.html', context)
