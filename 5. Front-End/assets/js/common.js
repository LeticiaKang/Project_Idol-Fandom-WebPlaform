jQuery(function() {
    // 글로벌 변수 선언
    const html = $('html');
    const header = $('#header');

    // AOS 효과 (Animate On Scroll)
    AOS.init({
        once: true
    });

    // 햄버거 메뉴 동작 (모바일)
    header.find('.hamburger-button').on('click', function () {
        if ( !header.hasClass('mobile-gnb--open') ) {
            header.addClass('mobile-gnb--open');
            html.addClass('scroll--prevent');
        } else {
            header.removeClass('mobile-gnb--open');
            html.removeClass('scroll--prevent');
        }
    });

    // 스크롤시 스티키 헤더 처리
    $(window).on('scroll', function () {
        let scrollTop = $(window).scrollTop();
        
        if ( scrollTop > 100 ) {
            if ( !header.hasClass('sticky') ) header.addClass('sticky');
        } else {
            header.removeClass('sticky');
        }
    })
    ;
});