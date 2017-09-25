coaches = { { :nialls, [] }, { :erin, [] }, { :mike, [] } }
students = ['kid 1', 'kid 2', 'kid 3', 'kid 4', 'kid 5', 'kid 6', 'kid 7']

#P1
defmodule CoachAssignment do

  def assign(coaches, students \\ [], cur_coach \\ 0)

  def assign(coaches, students, _ ) when students == [] do
    output_assignment(coaches)
  end

  def assign(coaches, students, cur_coach) do

    assignment = (elem(elem(coaches,cur_coach),1) ++ [hd(students)])
    assign( put_elem(coaches, cur_coach, {elem(elem(coaches,cur_coach),0), assignment}), students -- [hd(students)], (rem (cur_coach + 1), (tuple_size coaches) ))

  end

  def output_assignment(coaches) do
    IO.inspect coaches
  end
end

CoachAssignment.assign(coaches, students)