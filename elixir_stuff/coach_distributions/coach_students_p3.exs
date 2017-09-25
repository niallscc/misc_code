coaches = { { :nialls, [], 0.3 }, { :erin, [], 0.2 }, { :mike, [], 0.5 } }
students = ['kid 1', 'kid 2', 'kid 3', 'kid 4', 'kid 5', 'kid 6', 'kid 7','kid 8','kid 9','kid 10']

#P3
defmodule CoachAssignment do

  def assign(coaches, students \\ [], cur_coach \\ 0, student_count \\ 0)

  def assign(coaches, students, _, _) when students == [] do
    output_assignment(coaches)
  end

  def assign(coaches, students, cur_coach, student_count) do

    assignment = (elem(elem(coaches,cur_coach),1) ++ [hd(students)])
    if should_distribute(coaches, student_count, cur_coach) do
      updated = put_elem(coaches, cur_coach, {elem(elem(coaches,cur_coach),0), assignment,elem(elem(coaches,cur_coach),2) })
      assign(updated , students -- [hd(students)], (rem (cur_coach + 1),(tuple_size coaches)), student_count)
    else
      assign(coaches, students, (rem (cur_coach + 1), (tuple_size coaches)), student_count)
    end
  end

  def should_distribute(coaches, len_students, cur_coach) do

    if Float.ceil(elem(elem(coaches,cur_coach),2) * len_students) > length(elem(elem(coaches,cur_coach),1)) do
      true
    else
      false
    end
  end

  def output_assignment(coaches) do
    IO.inspect coaches
  end
end

CoachAssignment.assign(coaches, students, 0, length(students))