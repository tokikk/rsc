import PySimpleGUI as sg

sg.theme('Material2')

size1 = [[sg.Radio('割合', "RADIO1", font=("Meiryo UI", 14), default=True)],
        [
            sg.Text('  '),
            sg.InputText('100',
                         font=("Meiryo UI", 13),
                         size=(5, 1),
                         justification="right"),
            sg.Text('%')
        ]]

size2 = [[sg.Radio('絶対値', "RADIO1", font=("Meiryo UI", 14))],
        [
            sg.Text('  '),
            sg.InputText('100',
                         size=(5, 1),
                         font=("Meiryo UI", 13),
                         justification="right"),
            sg.Text('px  *  '),
            sg.InputText('100',
                         size=(5, 1),
                         font=("Meiryo UI", 13),
                         justification="right"),
            sg.Text('px')
        ]]

size_frame = [[sg.Column(size1), sg.Text('     '), sg.Column(size2)]]
path_frame = [[
    sg.InputText("",
                 key='PathField',
                 size=(33, 1),
                 text_color="black",
                 font=("Meiryo UI", 12),
                 disabled=True),
    sg.FolderBrowse('参照', key='SavedPath')
]]
input_frame = [[
    sg.Table([],
             headings=['ファイル'],
             auto_size_columns=False,
             def_col_width=5,
             num_rows=10,
             col_widths=[40],
             display_row_numbers=False,
             enable_events=True,
             header_text_color='#0000ff',
             header_background_color='#cccccc')
]]

layout = [[sg.Frame(
    '変換サイズ',
    size_frame,
    font=("Meiryo UI", 12),
)], [sg.Frame(
    '保存先',
    path_frame,
    font=("Meiryo UI", 12),
)],
[sg.Frame('変換対象', input_frame, font=("Meiryo UI", 12))],
          [
              sg.ProgressBar(100,
                             orientation='h',
                             size=(29, 20),
                             key='progressbar'),
              sg.Button(button_text='変換開始')
          ]]

window = sg.Window('サンプルプログラム', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED: #ウィンドウのXボタンを押したときの処理
        break
    if event == 'SavedPath':
        values['PathField'] = values['SavedPath']

window.close
