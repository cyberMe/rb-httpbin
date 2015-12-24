*** Settings ***
Documentation	Tests for httpbin.org
Library			HttpBin

*** Test Cases ***
auth
	[Documentation]	Test auth method
	:FOR	${user}	${password}	IN
	...		user	password
	...		user1	a2
    \	${var} = 	Test auth	${user}	${password}
    \	Should Be Equal As Integers	${var.code}	200
    \	Should Be Equal As Strings	${var.answer}	OK

get
	[Documentation]	Test get method
	${var} =	Test get	Host
	Should Be Equal As Integers	${var.code}	200
	Should Be Equal As Strings	${var.answer}	httpbin.org

stream
	[Documentation]	Test stream method
	${var} =	Test stream	20
	Should Be Equal As Integers	${var.code}	200
	Should Be Equal As Integers	${var.answer}	20
