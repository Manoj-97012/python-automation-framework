*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}      https://www.spicejet.com/
${BROWSER}  chrome

*** Test Cases ***
Verify the spicejet login page
    open browser    ${url}      ${BROWSER}
    click element    xpath://div[contains(text(),'Login')]
    input text    xpath://input[@data-testid='user-mobileno-input-box']     9701240422
    input text    xpath://input[@data-testid='password-input-box-cta']      Manoj@12345
    wait until element is visible    xpath://div[@class='css-1dbjc4n r-1awozwy r-z2wwpe r-1loqt21 r-18u37iz r-tmtnm0 r-1777fci r-1x0uki6 r-1w50u8q r-ah5dr5 r-1otgn73']
    page should contain    Login
    title should be