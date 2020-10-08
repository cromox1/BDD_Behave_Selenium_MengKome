Feature: Attempt to logging in with invalid credentials

    Scenario: None existing user try to login

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have an invalid user
        When I type username
        And I type password
        And I click on 'Login'
        Then I should see the error appeared
        And I close the browser

        # Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.

    Scenario: User try to login with wrong password

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a valid user
        When I type username
        And I type random password
        And I click on 'Login'
        Then I should see the error appeared
        And I close the browser

    Scenario: User try to login with no password

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have a valid user
        When I type username
        And I click on 'Login'
        Then I should see the text error 'Please fill out this filed.'
        And I close the browser

    Scenario: User try to login with no user

        Given I go to the site "mengkome.pythonanywhere.com"
        And I have no user
        When I type password
        And I click on 'Login'
        Then I should see the text error 'Please fill out this filed.'
        And I close the browser

    Scenario: User try to login without user

        Given I go to the site "mengkome.pythonanywhere.com"
        When I click on 'Login'
        Then I should see the text error 'Please fill out this filed.'
        And I close the browser

    Scenario: User try to login with invalid format user

        Given I go to the site "mengkome.pythonanywhere.com"
        When I type invalid format username
        And I type password
        And I click on 'Login'
        Then I should see the error appeared
        And I close the browser
