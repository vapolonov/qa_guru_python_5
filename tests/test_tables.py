from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
import time


def test_edit_web_tables():
    browser.open('/webtables')
    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Web Tables'))

    # adding 4th row
    s('#addNewRecordButton').click()
    s('#firstName').type('Vasiliy')
    s('#lastName').type('Apolonov')
    s('#userEmail').type('test@mail.com')
    s('#age').type('47')
    s('#salary').type('100000')
    s('#department').type('QA automation')
    s('#submit').click()

    ss('.rt-tr').element(4).ss('.rt-td').element(0).should(have.text('Vasiliy'))
    ss('.rt-tr').element(4).ss('.rt-td').element(1).should(have.text('Apolonov'))
    ss('.rt-tr').element(4).ss('.rt-td').element(3).should(have.text('test@mail.com'))
    ss('.rt-tr').element(4).ss('.rt-td').element(2).should(have.text('47'))
    ss('.rt-tr').element(4).ss('.rt-td').element(4).should(have.text('100000'))
    ss('.rt-tr').element(4).ss('.rt-td').element(5).should(have.text('QA automation'))

    # time.sleep(10)