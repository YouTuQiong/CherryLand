/**
 * Created by jordan on 10/5/2017.
 */
var banner = $('#banner')
// banner.on('click',function () {
//     console.log("2222")
// })
var all = $('.all-cover')
FastClick.attach(document.body);
var half = $('.half-cover')
banner.on("click", function () {
    all.fadeIn()
    half.fadeIn()
    banner.addClass('bannerReg')
    half.addClass('slideLeftReturn')
    console.log('++++++')
});
all.on('click', cover);

function cover() {
    $('.half-cover').fadeOut()
    $('.all-cover').fadeOut()
    half.removeClass('slideLeftReturn')
    half.addClass('slideLeft')
    banner.removeClass('bannerReg')
    console.log('---')

}
$(".swiperight").on("swiperight", function () {
    if (!half.hasClass('slideLeftReturn')) {
        all.fadeIn()
        half.fadeIn()
        banner.addClass('bannerReg')
        half.addClass('slideLeftReturn')
    }
});

function goTop() {
    $(window).scroll(function (e) {
        //若滚动条离顶部大于100元素
        if ($(window).scrollTop() > 400)
            $("#gotop").fadeIn(1000);//以1秒的间隔渐显id=gotop的元素
        else
            $("#gotop").fadeOut(1000);//以1秒的间隔渐隐id=gotop的元素
    });
};
function jump() {
    var event = event || window.event;//这里的event兼容跟上面不同，关于event的兼容，请猛戳这里
    if (event.keyCode === 13) {
    }
}
$(function () {
    //点击回到顶部的元素
    $("#gotop").click(function (e) {
        //以1秒的间隔返回顶部
        $('body,html').animate({scrollTop: 0}, 1000);
    });
    $("#gotop").mouseout(function (e) {
        $(gotop).addClass()
    });
    goTop();//实现回到顶部元素的渐显与渐隐
});
$(function () {
    function bannerOut() {
        var banner = $('#banner')
        var half = $('#half-cover')
        banner.click(function () {
            if (!banner.hasClass('bannerReg')) {
                half.addClass('slideLeftReturn')
            }
            else
                banner.addClass('bannerReg')
        })
        if (half.hasClass('slideLeftReturn')) {
            half.removeClass()
        }

    }

    function srcollToop(id) {
        var ie6 = document.all;
        var dv = $('#' + id), st;
        dv.attr('otop', dv.offset().top); //存储原来的距离顶部的距离
        dv.removeClass('swashIn')
        $(window).scroll(function () {
            st = Math.max(document.body.scrollTop || document.documentElement.scrollTop);
            if (st > parseInt(dv.attr('otop'))) {
                if (ie6) {//IE6不支持fixed属性，所以只能靠设置position为absolute和top实现此效果
                    dv.css({position: 'absolute', top: st});
                }
                else if (dv.css('position') != 'fixed') {
                    dv.css({'position': 'fixed', top: 20});
                    dv.addClass('slideUpReturn');
                    dv.css({"display": 'unset'})
                }
            } else if (dv.css('position') != 'static') {
                dv.removeClass('slideUpReturn');
                dv.css({'position': 'static'});
                // dv.css({"display":'none'})
            }
        });
    }

    srcollToop('textfloat')
    bannerOut()
});


$(function () {

    // Cache some selectors

    var clock = $('#clock'),
        alarm = clock.find('.alarm'),
        ampm = clock.find('.ampm');

    // Map digits to their names (this will be an array)
    var digit_to_name = 'zero one two three four five six seven eight nine'.split(' ');
    // This object will hold the digit elements
    var digits = {};

    // Positions for the hours, minutes, and seconds
    var positions = [
        'h1', 'h2', ':', 'm1', 'm2', ':', 's1', 's2'
    ];

    // Generate the digits with the needed markup,
    // and add them to the clock

    var digit_holder = clock.find('.digits');

    $.each(positions, function () {

        if (this == ':') {
            digit_holder.append('<div class="dots">');
        }
        else {

            var pos = $('<div>');

            for (var i = 1; i < 8; i++) {
                pos.append('<span class="d' + i + '">');
            }

            // Set the digits as key:value pairs in the digits object
            digits[this] = pos;

            // Add the digit elements to the page
            digit_holder.append(pos);
        }

    });

    // Add the weekday names

    var weekday_names = 'MON TUE WED THU FRI SAT SUN'.split(' '),
        weekday_holder = clock.find('.weekdays');

    $.each(weekday_names, function () {
        weekday_holder.append('<span>' + this + '</span>');
    });

    var weekdays = clock.find('.weekdays span');


    // Run a timer every second and update the clock

    (function update_time() {

        // Use moment.js to output the current time as a string
        // hh is for the hours in 12-hour format,
        // mm - minutes, ss-seconds (all with leading zeroes),
        // d is for day of week and A is for AM/PM
        var now = moment().format("HHmmssd");

        digits.h1.attr('class', digit_to_name[now[0]]);
        digits.h2.attr('class', digit_to_name[now[1]]);
        digits.m1.attr('class', digit_to_name[now[2]]);
        digits.m2.attr('class', digit_to_name[now[3]]);
        digits.s1.attr('class', digit_to_name[now[4]]);
        digits.s2.attr('class', digit_to_name[now[5]]);
        var dow = now[6];
        dow--;

        if (dow < 0) {
            dow = 6;
        }
        weekdays.removeClass('active').eq(dow).addClass('active');
        setTimeout(update_time, 1000);

    })();

    // Switch the theme
    //
    // $('a.button').click(function () {
    //     clock.toggleClass('ligh t dark');
    // });
    var search = $('#search')
    var s_text = $('#s_text')
    var inputs = $('#inputs')
    var event = event || window.event

    search.click(function () {
        s_text.css('display', 'initial')
        if (this.isShow === false) {
            $('.lo').css('z-index', '3')
            $('#s_text').css('z-index', '-3')
            this.isShow = true
            // $('#s_text').removeClass('tinUpIn')
            // $('#s_text').addClass('tinUpOut')
            // console.log('2223')
        }
        else {
            $('.lo').css('z-index', '-1')
            $('#s_text').css('z-index', '3')
            this.isShow = false
            // $('#s_text').removeClass('tinUpOut')
            // $('#s_text').addClass('tinUpIn')
            // console.log('2222')
        }

    })

});
