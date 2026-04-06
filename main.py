from flask import Flask, request, jsonify, send_from_directory, send_file
from sched import Scheduler, UpperScheduler
from other.vars import schedule, schedule_upper, data, classes
from excelgen import generate_timetable
import copy
import io

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/schedule', methods=['POST'])
def run_schedule():
    body = request.get_json()

    grades     = body['grades']
    rooms_low  = body['rooms_low']
    rooms_high = body['rooms_high']
    clusters   = body['clusters']

    has_low  = any(g <= 3 for g in grades)
    has_high = any(g >= 4 for g in grades)

    selected_data    = {k: v for k, v in data.items() if isinstance(k, str) and int(k[0]) in grades}
    selected_classes = {g: classes[g] for g in grades if g in classes}

    config = {
        "selected_grades": grades,
        "has_low":         has_low,
        "has_high":        has_high,
        "rooms_low":       rooms_low,
        "rooms_high":      rooms_high,
        "clusters":        clusters,
        "data":            selected_data,
        "classes":         selected_classes
    }

    wb = None

    if has_low:
        low_sched = copy.deepcopy(schedule)
        for day in low_sched:
            for _, info in low_sched[day].items():
                info["rooms"] = rooms_low.copy()

        low_config = {
            **config,
            "schedule": low_sched,
            "data":    {k: v for k, v in selected_data.items() if int(k[0]) <= 3},
            "classes": {g: selected_classes[g] for g in grades if g <= 3 and g in selected_classes}
        }

        wb = generate_timetable(
            Scheduler(config=low_config).exams(),
            title="Toetsweek Rooster FULLY CLAUDE CODED HAHAHAHEZ",
            output_path=None  # <-- zie hieronder
        )

    if has_high:
        upper_sched = copy.deepcopy(schedule_upper)
        for day in upper_sched:
            for _, info in upper_sched[day].items():
                info["rooms"] = rooms_high.copy()

        high_config = {
            **config,
            "schedule": upper_sched,
            "data":    {k: v for k, v in selected_data.items() if int(k[0]) > 3},
            "classes": {g: selected_classes[g] for g in grades if g > 3 and g in selected_classes}
        }

        wb = generate_timetable(
            UpperScheduler(config=high_config).exams(),
            title="Toetsweek Rooster — Bovenbouw",
            output_path=None
        )

    # Schrijf workbook naar memory buffer in plaats van naar disk
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='toetsweek_rooster.xlsx'
    )


if __name__ == '__main__':
    app.run(debug=True)
