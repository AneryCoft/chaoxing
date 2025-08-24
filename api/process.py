import time
from datetime import timedelta
from api.config import GlobalConst as gc



def show_progress(task_name: str, start_position: int, end_position: int, 
                 total_length: int, speed: float) -> None:
    """
    显示任务进度条，模拟任务进度。
    
    Args:
        task_name: 当前执行的任务名称
        start_position: 起始位置（以秒为单位）
        end_position: 结束位置（以秒为单位）
        total_length: 任务总长度（以秒为单位）
        speed: 任务执行速度
        
    Returns:
        None
    """
    start_time = time.time()
    duration = end_position - start_position
    expected_end_time = start_time + (duration / speed)
    
    while time.time() < expected_end_time:
        # 计算当前进度
        current_position = start_position + int((time.time() - start_time) * speed)
        percent_complete = min(int(current_position / total_length * 100), 100)
        
        # 生成进度条
        bar_length = 40
        filled_length = int(percent_complete * bar_length // 100)
        progress_bar = ("#" * filled_length).ljust(bar_length, " ")
        
        # 格式化输出进度信息
        progress_text = (
            f"\r当前任务: {task_name} |{progress_bar}| {percent_complete}%  "
            f"{timedelta(seconds=current_position)}/{timedelta(seconds=total_length)}"
        )
        
        print(progress_text, end="", flush=True)
        time.sleep(gc.DELAY)
