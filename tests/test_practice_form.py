import time

from selene import have, by, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_submit_automation_practice_form():
    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    s('#firstName').type('Vasiliy')
    s('#lastName').type('Apolonov')
    s('#userEmail').type('test@mail.com')
    s('#userNumber').type('9101112233')

    # Select Gender (radio-button)
    s('#genterWrapper').s('label[for=gender-radio-2]').click()
    time.sleep(1)
    s('#genterWrapper').s(by.text('Male')).click()

    # Select Date of Birth
    s('#dateOfBirthInput').click()
    s('.react-datepicker__year-select [value="1974"]').click()
    s('.react-datepicker__month-select [value="8"]').click()
    s('.react-datepicker__month .react-datepicker__week .react-datepicker__day--009').click()

    # Select Subjects
    subjects = ['Maths', 'English', 'Physics']
    for sub in subjects:
        s('#subjectsInput').set_value(sub).press_enter()

    # Select hobbies - checkbox
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-2]').click()
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-1]').click()

    # Load a file
    # s('#uploadPicture').send_keys('/tests/files/example.txt')

    # Filling the address
    s('#currentAddress').type('Russia, Nizhny Novgorod')
    s('#state').click()
    s(by.text('Uttar Pradesh')).click()
    s('#city').click()
    s(by.text('Lucknow')).click()

    # Sending the form
    s('#submit').perform(command.js.click)

    # Assertions
    s('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    # browser.all('.table-responsive tr').should(have.texts('Student Name Vasiliy Apolonov', 'Student Email test@mail.com'))
    s('.table-responsive').should(have.text('Vasiliy Apolonov'))
    s(".table-responsive").should(have.text('test@mail.com'))
    s(".table-responsive").should(have.text('Male'))
    s(".table-responsive").should(have.text('9101112233'))
    s(".table-responsive").should(have.text('09 September,1974'))
    s(".table-responsive").should(have.text('Maths, English, Physics'))
    s(".table-responsive").should(have.text('Reading, Sports'))
    s(".table-responsive").should(have.text('Russia, Nizhny Novgorod'))
    s(".table-responsive").should(have.text('Uttar Pradesh Lucknow'))













