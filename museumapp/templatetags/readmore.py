from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

import re

readmore_showscript = ''.join([
"this.parentNode.style.display='none';",
"this.parentNode.parentNode.getElementsByClassName('more')[0].style.display='inline';",
"return false;",
]);

@register.filter
def readmore(txt, showwords=15):
    global readmore_showscript
    words = re.split(r' ', escape(txt))

    if len(words) <= showwords:
        return txt

    # wrap the more part
    words.insert(showwords, '<span class="more" style="display:none;">')
    words.append('</span>')

    # insert the readmore part
    words.insert(showwords, '<div class="readmore small-text fira font-weight-bold sub-para"><a id="moreStuff" href="#" onclick="')
    words.insert(showwords+1, readmore_showscript)
    words.insert(showwords+2, '">read more</a>')
    words.insert(showwords+3, '</div>')


    return mark_safe(' '.join(words))

readmore.is_safe = False