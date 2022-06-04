# MazeEnv
OpenAIGym準拠の迷路環境　<br>
観測をプレイヤーから見た相対座標としている環境です　<br>

# 仕様
OpenAIGym準拠<br>
以下独自メソッド<br>
座標を引数に取り、その場所がその属性であるか判定するメソッド<br>
on_board　範囲内かどうか　Trueならマップ範囲内　Falseの部分は壁　どこがマップ内か指定する役目<br>
on_wall　壁のあるところ　通行不可　Trueのときに引数の座標が壁になる　<br>
on_minus　通行可能だが罰則のあるところの判定<br>
on_goal　ゴールの判定　ここにつくと終了<br>
is_visited　その座標に来たことがあるかどうか<br>

その他<br>
add_visited　引数の座標を到達済み座標として登録<br>
on_wallA　具体的な壁の実装の例<br>
on_wallB　具体的な壁の実装の例<br>

注意点<br>
reset内で環境をresetしたときに、ランダムに2種類の迷路のどちらかを生成する環境です<br>
観測はプレイヤーのいる場所に対する相対座標です<br>
