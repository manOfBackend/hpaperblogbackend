from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

forms = {'menus': [
            { 'className': 'head-blog', 'href': 'https://naver.com', 'name': 'Java' },
            { 'className': 'head-blog', 'href': 'https://naver.com', 'name': 'Spring' },
            { 'className': 'head-blog', 'href': 'https://naver.com', 'name': 'React.js' },
            { 'className': 'head-blog', 'href': 'https://naver.com', 'name': '방명록' }],
        'skills': [
            { 'iconValue': 'fab fa-java skill-icon java-style', 'name': 'JAVA', 'usage': 'Spring' },
            { 'iconValue': 'fab fa-vuejs skill-icon vue-style', 'name': '풀스택', 'usage': '웹 서비스' },
            { 'iconValue': 'far fa-chart-bar skill-icon analysis-style', 'name': '', 'usage': 'Database' }],
        'posts': [
            { 'imgSrc': 'https://images.unsplash.com/photo-1520038410233-7141be7e6f97?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ', 'href': 'http://naver.com', 'type': 'JAVA', 'format': '블로그', 'title': '자바 Optional의 ifPresent 활용하기', 'detail': '자바 8에 추가된 Option이 제공하는 ifPresent를 사용해 null을 체크하는 if 문을 줄이는 방법에 대해 설명합니다.' },
            { 'imgSrc': 'https://images.unsplash.com/photo-1580357991342-89ec1672c98a?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ', 'href': 'http://naver.com', 'type': 'TIPS', 'format': '블로그', 'title': '더 나은 개발자로 성장하는 방법, 에러 메시지를 읽으세요.', 'detail': '에러의 원인을 직접 분석하고 해결할 수 있는 개발자로 성장하려면 에러 메시지를 읽는 것부터 시작하세요.' },
            { 'imgSrc': 'https://images.unsplash.com/photo-1572470568265-4431ad3b2328?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ', 'href': 'http://naver.com', 'type': 'Spring', 'format': '블로그', 'title': '스프링 @트랜잭션과 스프링 AOP', 'detail': '스프링 @Transactional이 제대로 적용되지 않는 이유를 이해하려면 프록시 기반의 스프링 AOP에 대해 알아야 합니다.' },
            { 'imgSrc': 'https://images.unsplash.com/photo-1580894895938-bd31a62ed8ba?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ', 'href': 'http://naver.com', 'type': 'JPA', 'format': '블로그', 'title': 'JPA 사용시 엔티티 상태 확인하기', 'detail': 'JPA를 사용할 때 엔티티 상태가 Persistent 상태인지 확인하는 방법에 대해 설명합니다.' },
            { 'imgSrc': 'https://images.unsplash.com/photo-1502323777036-f29e3972d82f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ', 'href': 'http://naver.com', 'type': 'Spring', 'format': '블로그', 'title': '스프링 부트, 외부 설정 파일 우선 순위', 'detail': '스프링 부트가 지원하는 외부 설정 파일의 종류와 그 우선 순위에 대해 살펴봅니다.' }],
        'learning': [
            { 'imgSrc': 'https://www.fun-coding.org/style/images/ljh_python.png', 'href': 'https://www.inflearn.com/course/python-crawling-basic?inst=71325257', 'type': '파이썬/크롤링', 'format': '온라인 강의', 'title': '파이썬 입문과 크롤링기초 부트캠프', 'detail': '프로그래밍과 파이썬 기초 및 데이터를 프로그래밍으로 다루기' },
            { 'imgSrc': 'https://www.fun-coding.org/style/images/ljh_scrapy.png', 'href': 'https://www.inflearn.com/course/Crawling-Scrapy-Selenium?inst=469beff7', 'type': '크롤링중급', 'format': '온라인 강의', 'title': '파이썬과 Selenium / Scrapy', 'detail': '현존 최강 크롤링 기술과 프로그래밍 중급' },
            { 'imgSrc': 'https://www.fun-coding.org/style/images/mysql_python.png', 'href': 'https://www.inflearn.com/course/SQL-DB-MYSQL-파이썬-데이터분석?inst=7abfe3b0', 'type': 'MySQL/데이터베이스', 'format': '온라인 강의', 'title': 'SQL/DB(MySQL) 기본과 활용', 'detail': '데이터를 다루는 데이터베이스 기초와 파이썬 기반 활용' },
            { 'imgSrc': 'https://www.fun-coding.org/style/images/pandas.png', 'href': 'https://www.inflearn.com/course/파이썬-데이터분석-전처리-판다스-시각화?inst=65936339', 'type': 'pandas/plotly', 'format': '온라인 강의', 'title': '처음하는 파이썬 데이터 분석', 'detail': '데이터의 전처리부터 pandas, plotly (시각화), 분석 이론까지' },
            { 'imgSrc': 'https://www.fun-coding.org/style/images/progressing_open2.png', 'href': 'https://www.fun-coding.org', 'type': '머신러닝', 'format': '온라인 강의', 'title': '처음하는 머신러닝과 통계 기본', 'detail': '데이터 예측을 위한 머신러닝과 통계 기본' }],
        'title': 'Done is better than Perfect',
        'message': '일단 하자',
        'footerMessage': 'HyeonPaper',
        'contact': 'man.of.backend@gmail.com',
        'copyright': 'Copyright 2021 © All rights reserved.'
        }

@app.route('/forms')
def get_forms():
    return jsonify(forms)
    
