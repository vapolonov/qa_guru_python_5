from selene import have, be, command
from selene.support.shared import browser


def given_opened_text_box():
    browser.open()


def test_submit_form():
    browser.open('/text-box')
    browser.should(have.title('ToolsQA'))
    browser.should(have.title_containing('QA'))
    browser.element('.main-header').should(have.exact_text('Text Box'))
    browser.element('[class="main-header"]').should(have.text('Text'))
    browser.element('#userName').type('yasha')
    browser.element('#userEmail').type('test@test.com')
    browser.element('#currentAddress').type('Earth')
    browser.element('#permanentAddress').type('Universe & broad')
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    browser.execute_script(
        '''document.querySelectorAll("[id^=google_ads]"))
               .forEach(element => element.remove())'''
    )
    browser.execute_script(
        '''document.querySelectorAll("[id^=google_ads]"))
               .forEach(element => element.style.display = "none")'''
    )
    browser.execute_script(
        '''document.querySelectorAll("[id^=google_ads]"))
               .forEach(element => element.style.visibility = "hidden")'''
    )
    # при помощи вызова JS на самом элементе
    browser.element('[id^=google_ads]')._execute_script('element.remove()')

    # при помощи цикла for
    for ads in browser.all('[id^=google_ads]'):
        ads._execute_script('element.remove()')

    browser.all('#output p').should(have.texts(
        'yasha',
        'test@test.com',
        'Earth',
        'Universe & broad'
    ))
    browser.element('#currentAddress').should(have.text('Earth'))  # тест упадет
    browser.all('#currentAddress')[1].should(have.text('Earth'))
    browser.element('#output #currentAddress').should(have.text('Earth'))
    browser.element('#output').element('#currentAddress').should(have.text('Earth'))

