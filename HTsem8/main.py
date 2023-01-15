from pupil import Pupil
from Data import load_data, save_data
from UI import get_id, select, y_n
import UI_teacher as t
import UI_pupil as s


def main():
    data = load_db('data.json')
    pupils = [Pupil(**values) for values in data] if data else []
    search = {obj.surname: pupil_id for pupil_id, obj in enumerate(pupils)}
    while True:
        print("Начать работу?")
        if not y_n():
            break
        user = select()
        if user == 1:
            while True:
                action = t.input_action()
                if action == 4:
                    t.print_data(students)
                elif action == 3:
                    save_data('data.json', pupils)
                    break
                elif action == 2:
                    t.set_score(pupils[get_id(search)])
                else:  # action == 1:
                    pupils.append(t.add_pupil())
                    search[pupils[-1].surname] = len(pupils) - 1
        else:
            while True:
                action = s.input_action()
                if action == 1:
                    s.print_score(pupils[get_id(search)])
                else:  # action == 2:
                    break


if __name__ == "__main__":
    main()