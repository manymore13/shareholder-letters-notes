// 自定义 JavaScript

// 页面加载完成后执行
document.addEventListener("DOMContentLoaded", function() {
  // 为外部链接添加图标
  var links = document.querySelectorAll('a[href^="http"]');
  links.forEach(function(link) {
    if (!link.hostname.includes(window.location.hostname)) {
      link.innerHTML += ' <small>↗</small>';
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });

  // 添加平滑滚动
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });
});

// 数学公式支持
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]]
  },
  options: {
    processHtmlClass: 'arithmatex'
  }
};
