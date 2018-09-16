from django.db import models


# Create your models here.

class CompanyPage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    sub_heading = models.CharField(max_length=100, blank=True)
    header_image_1600x660 = models.ImageField(blank=True)
    image_600x400 = models.ImageField(blank=True)
    body = models.TextField(blank=True)

    sub_heading2 = models.CharField(max_length=100, blank=True)
    body2 = models.TextField(blank=True)

    accordion_title1 = models.CharField(max_length=100, blank=True)
    accordion_body1 = models.TextField(blank=True)
    accordion_title2 = models.CharField(max_length=100, blank=True)
    accordion_body2 = models.TextField(blank=True)
    accordion_title3 = models.CharField(max_length=100, blank=True)
    accordion_body3 = models.TextField(blank=True)

    home_page_image_800x1000 = models.ImageField(blank=True)


class TeamPage(models.Model):
    page_title = models.CharField(max_length=100, blank=True)
    sub_heading = models.CharField(max_length=100, blank=True)
    header_image_1600x660 = models.ImageField(blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.page_title

class TeamMember(models.Model):
    name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    image_350x350 = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    google_plus = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    ICONS = (
        ('flaticon-angry-bulldog-face', 'flaticon-angry-bulldog-face'),
        ('flaticon-animal', 'flaticon-animal'),
        ('flaticon-animal-1', 'flaticon-animal-1'),
        ('flaticon-animal-2', 'flaticon-animal-2'),
        ('.flaticon-animal-3', '.flaticon-animal-3'),
        ('flaticon-animal-4', 'flaticon-animal-4'),
        ('flaticon-animal-5', 'flaticon-animal-5'),
        ('flaticon-animal-6', 'flaticon-animal-6'),
        ('flaticon-animal-7', 'flaticon-animal-7'),
        ('flaticon-animal-8', 'flaticon-animal-8'),
        ('flaticon-animal-paw-print', 'flaticon-animal-paw-print'),
        ('flaticon-animals', 'flaticon-animals'),
        ('flaticon-animals-1', 'flaticon-animals-1'),
        ('flaticon-animals-2', 'flaticon-animals-2'),
        ('flaticon-animals-3', 'flaticon-animals-3'),
        ('flaticon-animals-4', 'flaticon-animals-4'),
        ('flaticon-animals-5', 'flaticon-animals-5'),
        ('flaticon-animals-6', 'flaticon-animals-6'),
        ('flaticon-animals-7', 'flaticon-animals-7'),
        ('flaticon-aquarium', 'flaticon-aquarium'),
        ('flaticon-basset-houd', 'flaticon-basset-houd'),
        ('flaticon-basset-hound-dog-head', 'flaticon-basset-hound-dog-head'),
        ('flaticon-bernese-mountain', 'flaticon-bernese-mountain'),
        ('flaticon-bird', 'flaticon-bird'),
        ('flaticon-border-collie', 'flaticon-border-collie'),
        ('flaticon-border-collie-head', 'flaticon-border-collie-head'),
        ('flaticon-brush', 'flaticon-brush'),
        ('flaticon-bulldog', 'flaticon-bulldog'),
        ('flaticon-bulldog-head', 'flaticon-bulldog-head'),
        ('flaticon-cat', 'flaticon-cat'),
        ('flaticon-chewing-bone-for-dog', 'flaticon-chewing-bone-for-dog'),
        ('flaticon-circle', 'flaticon-circle'),
        ('flaticon-dachshund', 'flaticon-dachshund'),
        ('flaticon-doberman-dog-head', 'flaticon-doberman-dog-head'),
        ('flaticon-dog', 'flaticon-dog'),
        ('flaticon-dog-1', 'flaticon-dog-1'),
        ('flaticon-dog-2', 'flaticon-dog-2'),
        ('flaticon-dog-3', 'flaticon-dog-3'),
        ('flaticon-dog-4', 'flaticon-dog-4'),
        ('flaticon-dog-5', 'flaticon-dog-5'),
        ('flaticon-dog-6', 'flaticon-dog-6'),
        ('flaticon-dog-7', 'flaticon-dog-7'),
        ('flaticon-dog-8', 'flaticon-dog-8'),
        ('flaticon-dog-and-pets-house', 'flaticon-dog-and-pets-house'),
        ('flaticon-dog-bone', 'flaticon-dog-bone'),
        ('flaticon-dog-bone-1', 'flaticon-dog-bone-1'),
        ('flaticon-dog-face', 'flaticon-dog-face'),
        ('flaticon-dog-head', 'flaticon-dog-head'),
        ('flaticon-dog-in-front-of-a-man', 'flaticon-dog-in-front-of-a-man'),
        ('flaticon-dog-kennel', 'flaticon-dog-kennel'),
        ('flaticon-dog-pet-allowed-hotel-signal', 'flaticon-dog-pet-allowed-hotel-signal'),
        ('flaticon-dog-puppy', 'flaticon-dog-puppy'),
        ('flaticon-dog-training', 'flaticon-dog-training'),
        ('flaticon-dog-training-1', 'flaticon-dog-training-1'),
        ('flaticon-dog-training-2', 'flaticon-dog-training-2'),
        ('flaticon-dog-training-3', 'flaticon-dog-training-3'),
        ('flaticon-dog-with-big-and-pointy-ears', 'flaticon-dog-with-big-and-pointy-ears'),
        ('flaticon-dog-with-chubby-cheeks', 'flaticon-dog-with-chubby-cheeks'),
        ('flaticon-dog-with-first-aid-kit-bag', 'flaticon-dog-with-first-aid-kit-bag'),
        ('flaticon-dog-with-floppy-ears', 'flaticon-dog-with-floppy-ears'),
        ('flaticon-dog-with-floppy-ears-1', 'flaticon-dog-with-floppy-ears-1'),
        ('flaticon-face-of-a-dog-with-sleepy-eyes', 'flaticon-face-of-a-dog-with-sleepy-eyes'),
        ('flaticon-face-of-staring-dog', 'flaticon-face-of-staring-dog'),
        ('flaticon-food', 'flaticon-food'),
        ('flaticon-guinea-pig-heag', 'flaticon-guinea-pig-heag'),
        ('flaticon-hamster', 'flaticon-hamster'),
        ('flaticon-hamster-1', 'flaticon-hamster-1'),
        ('flaticon-kurzhaar', 'flaticon-kurzhaar'),
        ('flaticon-laying-cat', 'flaticon-laying-cat'),
        ('flaticon-long-haired-dog-head', 'flaticon-long-haired-dog-head'),
        ('flaticon-man-combing-a-dog', 'flaticon-man-combing-a-dog'),
        ('flaticon-medical', 'flaticon-medical'),
        ('flaticon-mouse', 'flaticon-mouse'),
        ('flaticon-pawprint', 'flaticon-pawprint'),
        ('flaticon-pawprint-1', 'flaticon-pawprint-1'),
        ('flaticon-pet-carrier', 'flaticon-pet-carrier'),
        ('flaticon-pet-food', 'flaticon-pet-food'),
        ('flaticon-pet-friendly', 'flaticon-pet-friendly'),
        ('flaticon-pet-hotel-sign-with-a-dog-and-a-cat-under-a-roof-line',
         'flaticon-pet-hotel-sign-with-a-dog-and-a-cat-under-a-roof-line'),
        ('flaticon-pet-hotel-symbols-of-three-stars-a-semicircle-and-a-bone-black-shape',
         'flaticon-pet-hotel-symbols-of-three-stars-a-semicircle-and-a-bone-black-shape'),
        ('flaticon-pet-shelter', 'flaticon-pet-shelter'),
        ('flaticon-pets', 'flaticon-pets'),
        ('flaticon-pets-hotel-symbol-with-a-dog-and-a-cat-in-a-circle-with-one-star',
         'flaticon-pets-hotel-symbol-with-a-dog-and-a-cat-in-a-circle-with-one-star'),
        ('flaticon-play', 'flaticon-play'),
        ('flaticon-poodle', 'flaticon-poodle'),
        ('flaticon-rat', 'flaticon-rat'),
        ('flaticon-scissors', 'flaticon-scissors'),
        ('flaticon-siamese-cat', 'flaticon-siamese-cat'),
        ('flaticon-sign', 'flaticon-sign'),
        ('flaticon-sitting-rabbit', 'flaticon-sitting-rabbit'),
        ('flaticon-syringe', 'flaticon-syringe'),
        ('flaticon-toyger-cat', 'flaticon-toyger-cat'),
        ('flaticon-track', 'flaticon-track'),
        ('flaticon-turtle', 'flaticon-turtle'),
        ('flaticon-vet-with-cat', 'flaticon-vet-with-cat'),
        ('flaticon-veterinarian-hospital', 'flaticon-veterinarian-hospital'),
        ('flaticon-veterinary', 'flaticon-veterinary'),
        ('flaticon-walking-the-dog', 'flaticon-walking-the-dog'),
        ('flaticon-zynga-logotype', 'flaticon-zynga-logotype'),
    )

    icon = models.CharField(max_length=50, choices=ICONS, default='None')
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title
