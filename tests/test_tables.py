from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


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

    # edit second line
    s('#edit-record-2').click()
    s('#firstName').set_value('Ivan')
    s('#lastName').set_value('Sidorov')
    s('#userEmail').set_value('test@test.com')
    s('#age').set_value('28')
    s('#salary').set_value('50000')
    s('#department').set_value('HR')
    s('#submit').click()

    ss('.rt-tr').element(2).ss('.rt-td').element(0).should(have.text('Ivan'))
    ss('.rt-tr').element(2).ss('.rt-td').element(1).should(have.text('Sidorov'))
    ss('.rt-tr').element(2).ss('.rt-td').element(3).should(have.text('test@test.com'))
    ss('.rt-tr').element(2).ss('.rt-td').element(2).should(have.text('28'))
    ss('.rt-tr').element(2).ss('.rt-td').element(4).should(have.text('50000'))
    ss('.rt-tr').element(2).ss('.rt-td').element(5).should(have.text('HR'))

    # delete third line
    s('#delete-record-3').click()

    s('.rt-tbody').ss('.rt-tr-group')[2].should(have.no.text('Kierra\nGentry\n29\nkierra@example.com\n2000\nLegal'))

