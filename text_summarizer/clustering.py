from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
class Cluster:
    def optimalK(self, data, nrefs=3, maxClusters=15):
        """
        Calculates KMeans optimal K using Gap Statistic
        Params:
            data: ndarry of shape (n_samples, n_features)
            nrefs: number of sample reference datasets to create
            maxClusters: Maximum number of clusters to test for
        Returns: (gaps, optimalK)
        """
        gaps = np.zeros((len(range(1, maxClusters)),))
        resultsdf = pd.DataFrame({'clusterCount':[], 'gap':[]})
        for gap_index, k in enumerate(range(1, maxClusters)):
    # Holder for reference dispersion results
            refDisps = np.zeros(nrefs)
    # For n references, generate random sample and perform kmeans getting resulting dispersion of each loop
            for i in range(nrefs):

                # Create new random reference set
                randomReference = np.random.random_sample(size=data.shape)

                # Fit to it
                km = KMeans(k)
                km.fit(randomReference)

                refDisp = km.inertia_
                refDisps[i] = refDisp
    # Fit cluster to original data and create dispersion
            km = KMeans(k)
            km.fit(data)

            origDisp = km.inertia_
    # Calculate gap statistic
            gap = np.log(np.mean(refDisps)) - np.log(origDisp)
    # Assign this loop's gap statistic to gaps
            gaps[gap_index] = gap

            resultsdf = resultsdf.append({'clusterCount':k, 'gap':gap}, ignore_index=True)
        return (gaps.argmax() + 1, resultsdf)

    def bestK(self, tfidf_matrix, text):
        Sum_of_squared_distances = []
        slope = []
        clusters = []
        inertia = []
        print(len(text))

        clusters, df = self.optimalK(data=tfidf_matrix, nrefs=10, maxClusters=int(len(text)/10))
        df.to_csv("haha.csv")

        clusters=int(df[df['gap']==df['gap'].max()]['clusterCount'].values[0])
        lst = df['gap'].values
        idx = (np.abs(lst - df['gap'].mean())).argmin()
        clusters = int(df[df['gap']==lst[idx]]['clusterCount'].values[0])
        print(clusters)
        #if int(len(text)/3)>0:
        #    if clusters>=int(len(text)/3):
        #        if int(len(text)/9)>0:
        #            clusters = int(len(text)/9)
        #        else:
        #            clusters = int(len(text)/6)
        #        print("Phase 1")
        #    elif clusters >= int(len(text)/10):
        #        lst = df['gap'].values
        #        idx = (np.abs(lst - df['gap'].mean())).argmin()
        #        clusters = int(df[df['gap']==lst[idx]]['clusterCount'].values[0])
        #        print("Phase 2")
        #    elif clusters >= int(len(text)/10):
        #        clusters = int(len(text)/10)
        #        print("Phase 3")
        #    else:
        #        clusters=len(text)
        #        print("Phase 4")
        #else:
        #    clusters = int(len(text))
        print(clusters)
        km = KMeans(n_clusters=clusters)
        km = km.fit(tfidf_matrix)
        results = km.predict(tfidf_matrix)
        df = pd.DataFrame({'text': text, 'results': results})

        #for k in range(1,len(text)-1):
        #    slope.append(np.polyfit([k, k+1],[Sum_of_squared_distances[k-1], Sum_of_squared_distances[k]], 1)[0])
        #    clusters.append(k)
        #df = pd.DataFrame({'clus':clusters, 'slope': slope})
        df.to_csv("hehe.csv")
        return df
        #plt.plot(df['clus'], df['inertia'])
        #plt.show()
