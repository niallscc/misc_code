coaches = { { :nialls, ['kid 9'] }, { :erin, [] }, { :mike, ['kid 10'] } }
students = ['kid 1', 'kid 2', 'kid 3', 'kid 4', 'kid 5', 'kid 6', 'kid 7']

#P2
defmodule CoachAssignment do

  def assign(coaches, students \\ [], cur_coach \\ 0)

  def assign(coaches, students, _ ) when students == [] do
    output_assignment(coaches)
  end

  def assign(coaches, students, cur_coach) do

    assignment = (elem(elem(coaches,cur_coach),1) ++ [hd(students)])
    cur_coach_count = length(elem(elem(coaches,cur_coach),1))
    min_count = min_coach_count(coaches,10000,0)
    if cur_coach_count <= min_count do
      assign( put_elem(coaches, cur_coach, {elem(elem(coaches,cur_coach),0), assignment}), students -- [hd(students)], (rem (cur_coach + 1),(tuple_size coaches)))
    else
      assign(coaches, students, (rem (cur_coach + 1), (tuple_size coaches)))
    end
  end

  def min_coach_count(coaches, min_count, n)do
    if n < (tuple_size coaches) do
      len = length(elem(elem(coaches,n),1))
      if len < min_count do
        min_coach_count(coaches,len, n+1)
      else
        min_coach_count(coaches, min_count, n+1)
      end
    else
      min_count
    end
  end

  def output_assignment(coaches) do
    IO.inspect coaches
  end
end

CoachAssignment.assign(coaches, students)