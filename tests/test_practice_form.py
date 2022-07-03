import time

from selene import have, by, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class Subjects:
    maths = 'Maths'
    english = 'English'
    physics = 'Physics'


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
    '''
    OR:
    gender_group = s('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text('Male')).click()
    '''

    # Select Date of Birth
    s('#dateOfBirthInput').click()
    s('.react-datepicker__year-select').s('[value="1974"]').click()
    s('.react-datepicker__month-select').s('[value="8"]').click()
    s('.react-datepicker__day--009').click()

    '''
    browser.execute_script('document.querySelector("#dateOfBirthInput").value = "27 Jun 2022";')
    browser.element('#dateOfBirthInput').perform(command.js.set_value('09 Sep 1974')).press_enter()
    browser.element('#dateOfBirthInput').with_(set_value_by_js=True).set_value('09 Sep 1974')
    '''


    # Select Subjects
    s('#subjectsInput').set_value(Subjects.maths).press_enter()
    s('#subjectsInput').set_value(Subjects.english).press_enter()
    s('#subjectsInput').set_value(Subjects.physics).press_enter()

    # Select hobbies - checkbox
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-2]').click()
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-1]').click()

    '''
    # OR
    music_hobby = browser.element('#hobbies-checkbox-1')
    music_hobby.click()

    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    '''

    # Load a file

    import os
    s('#uploadPicture').send_keys(os.path.abspath('../resources/example.txt'))

    '''
    ABSOLUTE PATH:
    s('#uploadPicture').send_keys('C:\\temp\\example.txt')
    '''

    '''
    OR:
    def resource(path):
        from pathlib import Path
        import demoqa_tests
        return str(
            Path(demoqa_tests.__file__).
            parent.
            parent.
            joinpath(f'resources/{path}'))

    browser.element('#uploadPicture').send_keys(resource('example.txt'))
    '''

    # Filling the address
    s('#currentAddress').type('Russia, Nizhny Novgorod')
    s('#state').click()
    s(by.text('Uttar Pradesh')).click()
    s('#city').click()
    s(by.text('Lucknow')).click()

    # Sending the form
    '''
    # s('footer').perform(command.js.remove)
    # s('#submit').click()
    '''
    s('#submit').perform(command.js.click)

    # Assert
    s('.table-responsive').should(have.text('Vasiliy Apolonov'))
    s('.table-responsive').should(have.text('test@mail.com'))
    s('.table-responsive').should(have.text('Male'))
    s('.table-responsive').should(have.text('9101112233'))
    s('.table-responsive').should(have.text('09 September,1974'))
    s('.table-responsive').should(have.text('Maths, English, Physics'))
    s('.table-responsive').should(have.text('Reading, Sports'))
    s('.table-responsive').should(have.text('example.txt'))
    s('.table-responsive').should(have.text('Russia, Nizhny Novgorod'))
    s('.table-responsive').should(have.text('Uttar Pradesh Lucknow'))

    '''
    OR
    s('.table').ss('tr').should(have.texts('Values',
                                           'Vasiliy Apolonov',
                                           'test@mail.com',
                                           'Male',
                                           '9101112233',
                                           '09 September,1974',
                                           'Maths, English, Physics',
                                           'Reading, Sports',
                                           'example.txt',
                                           'Russia, Nizhny Novgorod',
                                           'Uttar Pradesh Lucknow'))
    '''

    browser.all('table tr')[5].all('td')[1].should(have.exact_text('09 September,1974'))

    def cells_of_row(index, should_have_texts: list[str]):
        browser.element('.modal-dialog').all('table tr')[index].all('td').should(have.exact_texts(*should_have_texts))

    cells_of_row(index=5, should_have_texts=[
        'Date of Birth', '09 September,1974'
    ])

    cells_of_row(index=6, should_have_texts=['Subjects', 'Maths, English, Physics'])
