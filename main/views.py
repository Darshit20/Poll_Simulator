from django.shortcuts import render
from django.views import View

# Create your views here.
candidates=[]
voters=[]
vote_dict={}

def home(request):
    return render(request, 'home.html')


def add_candidate(request):
    template_name = 'add_candidate.html'
    if request.method=='POST':
        cname=request.POST['cname']
        # self.candidate.clear()
        if cname.upper() in (name.upper() for name in candidates):
            print(candidates)
            return render(request, template_name, {"err":"Already Added.."})
        else:
            candidates.append(cname)
            print(candidates)
            vote_dict[cname]="0"
            return render(request, template_name, {"suc":"Candidate Added.."})
    else:
        return render(request, template_name)


def vote_candidate(request):
    template_name = 'vote_candidate.html'
    if request.method=='POST':
        voter=str(request.POST['vname'])
        cd = request.POST['candidate']

        if voter in voters:
            print(voters)
            data = {
                "msg": voter+", you have already voted!",
                "candidate":candidates
            }
            return render(request, template_name, data)
        else:
            voters.append(voter)

            print(voters)
            data = {
                "msg": voter+", your vote has been recorded successfully.",
                "candidate":candidates
            }
            vote_count= int(vote_dict[cd])
            vote_count+=1
            vote_dict[cd]=vote_count

            print(vote_dict)
            return render(request, template_name, data)
    else:   
        return render(request, template_name, {"candidate":candidates})


def vote_result(request):
    template_name = 'vote_result.html'
    sort_dict = sorted(vote_dict.items(), key=lambda x: x[1], reverse=True)
    return render(request, template_name, {"data":sort_dict})



def vote_summary(request):
    template_name = 'vote_summary.html'
    return render(request, template_name, {"data":vote_dict})


# class admin(View):
#     template_name = 'add_candidate.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         cname=request.POST['cname']
#         # self.candidate.clear()
#         if cname.upper() in (name.upper() for name in candidates):
#             print(candidates)
#             return render(request, self.template_name, {"err":"Already Added.."})
#         else:
#             candidates.append(cname)
#             print(candidates)
#             vote_dict[cname]="0"
#             return render(request, self.template_name, {"suc":"Candidate Added.."})

# class candidate(View):
#     template_name = 'vote_candidate.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, {"candidate":candidates})

#     def post(self, request, *args, **kwargs):
#         voter=str(request.POST['vname'])
#         cd = request.POST['candidate']

#         if voter in voters:
#             print(voters)
#             data = {
#                 "msg": voter+", you have already voted!",
#                 "candidate":candidates
#             }
#             return render(request, self.template_name, data)
#         else:
#             voters.append(voter)

#             print(voters)
#             data = {
#                 "msg": voter+", your vote has been recorded successfully.",
#                 "candidate":candidates
#             }
#             vote_count= int(vote_dict[cd])
#             vote_count+=1
#             vote_dict[cd]=vote_count

#             print(vote_dict)
#             return render(request, self.template_name, data)
