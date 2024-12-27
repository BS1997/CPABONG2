CKEDITOR.stylesSet.add('my_styles', [
    {
        name: '회색막대 제목',
        element: 'h3',
        styles: {
            'border-left': '4px solid #ccc',
            'padding-left': '10px',
            'margin': '20px 0',
            'font-weight': 'bold'
        }
    },
    {
        name: '내 부제목',  // Subtitle 그룹에 추가될 새로운 스타일
        element: 'h4',
        attributes: {
            'class': 'my-subtitle'
        }
    }
]);