from django.test import TestCase

class AccountTests(TestCase):
    def setUp(self):
    # Create a user
    self.user = User.objects.create_user(
        email='test@example.com',
        password='test123',
        first_name='Test',
        last_name='User',
    )
    
    # Add some data to the database
    self.address = Address.objects.create(
        customer=self.user,
        street_address='123 Main St',
        city='Anytown',
        state='CA',
        zip_code='12345',
    )

    def tearDown(self):
    # Delete the user and address created during the tests
    self.user.delete()
    self.address.delete()

    # Create your tests here.
    def test_user_registration(self):
        # Test that the form displays correctly and all fields are present
        response = self.client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/registration/register.html')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, 'type="submit"')
        
        # Test that the form correctly validates and displays errors for incomplete or invalid data
        response = self.client.post(reverse('account:register'), {'email': 'invalid'})
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        
        # Test that the form correctly creates a new user and activates the user's account when valid data is submitted
        response = self.client.post(reverse('account:register'), {'email': 'valid@email.com', 'password1': 'password', 'password2': 'password'})
        self.assertRedirects(response, reverse('account:register_email_confirm'))
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.email, 'valid@email.com')
        self.assertTrue(user.is_active)
        
        # Test that the form correctly sends an email to the user with an account activation link
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Activate your Account')
        self.assertEqual(mail.outbox[0].to, ['valid@email.com'])
        self.assertIn('account/registration/account_activation_email.html', mail.outbox[0].body)

    def test_register_form_displays_correctly(self):
        # Send a GET request to the registration form
        response = self.client.get('/account/register/')

        # Check that the form is displayed correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/registration/register.html')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, 'type="submit"')

    def test_register_form_validates_incomplete_data(self):
        # Send a POST request to the registration form with incomplete data
        response = self.client.post('/account/register/', data={'first_name': 'Test'})

        # Check that the form displays errors for incomplete data
        self.assertFormError(response, 'form', 'last_name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'password1', 'This field is required.')
        self.assertFormError(response, 'form', 'password2', 'This field is required.')

    def test_register_form_creates_new_user(self):
        # Send a POST request to the registration form with valid data
        response = self.client.post('/account/register/', data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'test123',
            'password2': 'test123',
        })

        # Check that a new user was created and their account was activated
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/account/registration_confirmed')
        self.assertEqual(User.objects.count(), 2)  # There is already one user in the database from setUp
        new_user = User.objects.get(email='testuser@example.com')
        self.assertTrue(new_user.is_active)

    def test_user_registration(self):
        # Test that the form displays correctly and all fields are present
        response = self.client.get(reverse('account:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/registration/register.html')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, 'type="submit"')
        self.assertContains(response, 'type="email"')
        self.assertContains(response, 'type="password"')

        # Test that the form correctly validates and displays errors for incomplete or invalid data
        response = self.client.post(reverse('account:register'), {'email': 'invalid'})
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        response = self.client.post(reverse('account:register'), {'password1': 'short'})
        self.assertFormError(response, 'form', 'password1', 'This password is too short. It must contain at least 8 characters.')
        response = self.client.post(reverse('account:register'), {'password1': 'password1', 'password2': 'password2'})
        self.assertFormError(response, 'form', 'password2', "The two password fields didn't match.")

        # Test that the form correctly creates a new user and activates the user's account when valid data is submitted
        response = self.client.post(reverse('account:register'), {'email': 'user@example.com', 'password1': 'password', 'password2': 'password'}, follow=True)
        self.assertRedirects(response, reverse('account:register_email_confirm'))
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.email, 'user@example.com')
        self.assertTrue(user.is_active)

        # Test that the form correctly sends an email to the user with an account activation link
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to, ["john.doe@example.com"])
        self.assertEqual(email.subject, "Activate your Account")
        self.assertIn("Please click on the link below to activate your account:", email.body)
        self.assertIn(f"http://example.com/account/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/", email.body)

###########################################################################################################
    def test_login_form(self):
        # Test that the login form displays correctly and all fields are present
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, 'type="text"')
        self.assertContains(response, 'type="password"')
        
        # Test that the form correctly validates and displays errors for incomplete or invalid data
        response = self.client.post(reverse('account:login'), {'username': '', 'password': ''})
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')
        
        # Test that the form correctly logs in the user with valid credentials
        User.objects.create_user(username='testuser', password='testpass')
        response = self.client.post(reverse('account:login'), {'username': 'testuser', 'password': 'testpass'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/dashboard/dashboard.html')
        self.assertContains(response, 'Welcome, testuser')
        
        # Test that the form displays an error message when invalid credentials are submitted
        response = self.client.post(reverse('account:login'), {'username': 'testuser', 'password': 'wrongpass'})
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
